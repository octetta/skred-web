function applyANSI(text) {
    if (text.indexOf('\x1b[') === -1) {
        return text;
    }
    const parts = text.split(/\x1b\[([0-9;]+)m/);
    return parts;
}
console.log(applyANSI("hello \x1b[38;2;255;0;0mworld\x1b[0m!"));
