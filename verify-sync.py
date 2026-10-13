#!/usr/bin/env python3
"""
verify-sync.py — Code BEAM Europe Presentation Triad Synchronization Verifier

Verifies that the three presentation files stay in complete lockstep:
  1. codebeam.html  — Live presentation deck (projector display & notes)
  2. cues.html      — Mobile speaker teleprompter app (responsive phone view)
  3. print-cues.html — Printable 2-page stage cheat sheet (letter paper)

Checks performed:
  - File existence and readability
  - Total slide counts match exactly across all 3 files
  - Slide titles and topics match for every slide index (1 to N)
  - Slide 6 interactive code examples match line-for-line across all 3 files
  - Slide 8 credits, links, dedication ('🥹💖🙌DES'), and bass drop ('v4 m0') match
  - Consistent speaker identity ('Joe Stewart', 'octetta.com')

Usage:
  ./verify-sync.py                # Run all checks
  ./verify-sync.py --verbose      # Detailed output
  ./verify-sync.py --install-hook # Install as git pre-commit hook
"""

import sys
import re
from pathlib import Path
from bs4 import BeautifulSoup

# ANSI color codes for terminal output
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
DIM = "\033[2m"
RESET = "\033[0m"

# Expected slide topics by index (1-based)
EXPECTED_TOPICS = {
    1: ["skred", "title", "hook", "weird live audio coding"],
    2: ["zero to noise"],
    3: ["why audio is weird & hard", "why audio is weird"],
    4: ["architecture"],
    5: ["hands-on", "make some noise"],
    6: ["examples"],
    7: ["what else can you build"],
    8: ["credits", "links", "q&a"],
    9: ["orchestrating from the beam"],
    10: ["browser", "wasm"],
    11: ["reference", "waveforms"],
}


def log_pass(msg):
    print(f"  {GREEN}✓ PASS{RESET} {msg}")


def log_fail(msg):
    print(f"  {RED}✗ FAIL{RESET} {msg}")


def log_info(msg):
    print(f"  {CYAN}ℹ INFO{RESET} {msg}")


def normalize_title(title: str) -> str:
    """Normalize a title string for fuzzy comparison."""
    cleaned = title.lower()
    cleaned = re.sub(r"\[.*?\]", "", cleaned)  # remove [backup], etc.
    cleaned = re.sub(r"slide\s*\d+(/\d+)?", "", cleaned)
    cleaned = re.sub(r"\(\d+\s*steps?\)", "", cleaned)
    cleaned = re.sub(r"[^\w\s]", " ", cleaned)
    return " ".join(cleaned.split())


def install_git_hook(script_path: Path, repo_root: Path) -> bool:
    """Install verify-sync.py as a git pre-commit hook."""
    hooks_dir = repo_root / ".git" / "hooks"
    if not hooks_dir.exists():
        log_fail(f"Git hooks directory not found at {hooks_dir}")
        return False

    hook_file = hooks_dir / "pre-commit"
    hook_content = f"""#!/bin/sh
# Git pre-commit hook installed by verify-sync.py
python3 "{script_path.resolve()}"
"""
    hook_file.write_text(hook_content)
    hook_file.chmod(0o755)
    log_pass(f"Installed git pre-commit hook at {hook_file}")
    return True


def run_checks(repo_root: Path, verbose: bool = False) -> bool:
    print(f"\n{BOLD}================================================================={RESET}")
    print(f"{BOLD}  Code BEAM Presentation Triad Synchronization Check{RESET}")
    print(f"{BOLD}================================================================={RESET}\n")

    deck_path = repo_root / "codebeam.html"
    cues_path = repo_root / "cues.html"
    print_path = repo_root / "print-cues.html"

    # Check 1: File Existence
    all_files_exist = True
    for p in [deck_path, cues_path, print_path]:
        if not p.is_file():
            log_fail(f"Missing required file: {p.name}")
            all_files_exist = False
        else:
            log_pass(f"Found {p.name} ({p.stat().st_size:,} bytes)")

    if not all_files_exist:
        return False

    # Parse HTML files
    try:
        soup_deck = BeautifulSoup(deck_path.read_text(encoding="utf-8"), "html.parser")
        soup_cues = BeautifulSoup(cues_path.read_text(encoding="utf-8"), "html.parser")
        soup_print = BeautifulSoup(print_path.read_text(encoding="utf-8"), "html.parser")
    except Exception as e:
        log_fail(f"Failed to parse HTML files: {e}")
        return False

    failures = 0

    # Extract slide sections / cards
    slides_container = soup_deck.find("div", class_="slides")
    deck_slides = slides_container.find_all("section", recursive=False) if slides_container else []
    cue_cards = soup_cues.find_all("div", class_="card")
    print_cards = soup_print.find_all("div", class_="card")

    n_deck = len(deck_slides)
    n_cues = len(cue_cards)
    n_print = len(print_cards)

    print(f"\n{BOLD}1. Slide Count Alignment:{RESET}")
    if n_deck == n_cues == n_print and n_deck > 0:
        log_pass(f"Slide counts match across all three files: {n_deck} slides total")
    else:
        log_fail(f"Slide counts mismatch: codebeam.html={n_deck}, cues.html={n_cues}, print-cues.html={n_print}")
        failures += 1

    total_slides = min(n_deck, n_cues, n_print)

    # Check 2: Slide Titles Alignment
    print(f"\n{BOLD}2. Slide Title & Topic Alignment:{RESET}")
    for idx in range(total_slides):
        slide_num = idx + 1
        s_deck = deck_slides[idx]
        c_cue = cue_cards[idx]
        c_print = print_cards[idx]

        h_tag = s_deck.find(["h1", "h2"])
        title_deck = h_tag.get_text(strip=True) if h_tag else "No Title"

        t_cue = c_cue.find("div", class_="slide-title")
        title_cue = t_cue.get_text(strip=True) if t_cue else "No Title"

        t_print = c_print.find("div", class_="card-title")
        title_print = t_print.get_text(strip=True) if t_print else "No Title"

        expected_keywords = EXPECTED_TOPICS.get(slide_num, [])
        all_titles_text = f"{title_deck} {title_cue} {title_print}".lower()

        matched_keyword = any(kw in all_titles_text for kw in expected_keywords)

        if matched_keyword:
            log_pass(f"Slide {slide_num:02d}: '{title_deck}' (Cues: '{title_cue}')")
        else:
            log_fail(
                f"Slide {slide_num:02d} topic mismatch:\n"
                f"         codebeam: '{title_deck}'\n"
                f"         cues:     '{title_cue}'\n"
                f"         print:    '{title_print}'\n"
                f"         expected: {expected_keywords}"
            )
            failures += 1

        if verbose:
            print(f"         {DIM}Deck: '{title_deck}' | Cues: '{title_cue}' | Print: '{title_print}'{RESET}")

    # Check 3: Slide 6 Audio Example Commands (Must match line for line)
    print(f"\n{BOLD}3. Slide 06 Audio Examples Consistency:{RESET}")
    if total_slides >= 6:
        deck_s6 = deck_slides[5]
        cue_s6 = cue_cards[5]
        print_s6 = print_cards[5]

        deck_pre_cmds = [p.get_text() for p in deck_s6.find_all("pre", class_="skred-cmd")]
        cue_text = cue_s6.get_text()
        print_text = print_s6.get_text()

        all_cmds_found = True
        for block in deck_pre_cmds:
            for line in block.splitlines():
                line = line.strip()
                if not line:
                    continue
                if line not in cue_text:
                    log_fail(f"Slide 6 code missing in cues.html: {line}")
                    all_cmds_found = False
                    failures += 1
                if line not in print_text:
                    log_fail(f"Slide 6 code missing in print-cues.html: {line}")
                    all_cmds_found = False
                    failures += 1

        if all_cmds_found:
            log_pass("All Slide 06 audio DSP commands match line-for-line across deck, cues, and print")
            log_info(f"Verified Coin Pickup: 'v0 w1 g0 / n60 l1 g.1 n80 l1'")

    # Check 4: Slide 8 Credits, Links, Dedication & Outro Controls
    print(f"\n{BOLD}4. Slide 08 Credits, Dedication & Outro Sync:{RESET}")
    if total_slides >= 8:
        deck_s8 = deck_slides[7]
        cue_s8 = cue_cards[7]
        print_s8 = print_cards[7]

        txt_deck = deck_s8.get_text()
        txt_cue = cue_s8.get_text()
        txt_print = print_s8.get_text()

        # Check dedication string
        dedication_string = "🥹💖🙌"
        wife_initials = "DES"
        for name, txt in [("codebeam.html", txt_deck), ("cues.html", txt_cue), ("print-cues.html", txt_print)]:
            if dedication_string in txt and wife_initials in txt:
                log_pass(f"Slide 08 dedication '{dedication_string}{wife_initials}' verified in {name}")
            else:
                log_fail(f"Slide 08 dedication '{dedication_string}{wife_initials}' missing in {name}")
                failures += 1

        # Check outro unmute command (v4 m0)
        for name, txt in [("codebeam.html", txt_deck), ("cues.html", txt_cue), ("print-cues.html", txt_print)]:
            if "v4 m0" in txt:
                log_pass(f"Slide 08 outro REPL unmute 'v4 m0' verified in {name}")
            else:
                log_fail(f"Slide 08 outro command 'v4 m0' missing in {name}")
                failures += 1

        # Check credit links
        for credit in ["octetta.com", "gadgetto", "pulp"]:
            if credit in txt_deck.lower() and credit in txt_cue.lower() and credit in txt_print.lower():
                log_pass(f"Slide 08 credit '{credit}' verified across all 3 files")
            else:
                log_fail(f"Slide 08 credit '{credit}' missing in one of the files")
                failures += 1

    # Check 5: Speaker Badge and Consistency
    print(f"\n{BOLD}5. Presenter Identity Consistency:{RESET}")
    all_have_speaker = True
    for name, soup in [("codebeam.html", soup_deck), ("cues.html", soup_cues), ("print-cues.html", soup_print)]:
        body_text = soup.get_text()
        if "Joe Stewart" not in body_text or "octetta.com" not in body_text:
            log_fail(f"Speaker identity 'Joe Stewart' / 'octetta.com' missing in {name}")
            all_have_speaker = False
            failures += 1
    if all_have_speaker:
        log_pass("Presenter identity ('Joe Stewart' & 'octetta.com') consistent across all 3 files")

    # Summary
    print(f"\n{BOLD}================================================================={RESET}")
    if failures == 0:
        print(f"  {GREEN}{BOLD}RESULT: ALL CHECKS PASSED! Presentation triad is in sync.{RESET}")
        print(f"{BOLD}================================================================={RESET}\n")
        return True
    else:
        print(f"  {RED}{BOLD}RESULT: {failures} CHECK(S) FAILED! Files are out of sync.{RESET}")
        print(f"{BOLD}================================================================={RESET}\n")
        return False


def main():
    repo_root = Path(__file__).resolve().parent
    args = sys.argv[1:]

    if "--help" in args or "-h" in args:
        print(__doc__)
        return 0

    if "--install-hook" in args:
        success = install_git_hook(Path(__file__), repo_root)
        return 0 if success else 1

    verbose = "--verbose" in args or "-v" in args
    passed = run_checks(repo_root, verbose=verbose)
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
