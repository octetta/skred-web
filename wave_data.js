const waves = [
  {
    "id": 0,
    "name": "sine",
    "type": "Basic Synth",
    "one_shot": false
  },
  {
    "id": 1,
    "name": "square",
    "type": "Basic Synth",
    "one_shot": false
  },
  {
    "id": 2,
    "name": "saw-down",
    "type": "Basic Synth",
    "one_shot": false
  },
  {
    "id": 3,
    "name": "saw-up",
    "type": "Basic Synth",
    "one_shot": false
  },
  {
    "id": 4,
    "name": "triangle",
    "type": "Basic Synth",
    "one_shot": false
  },
  {
    "id": 5,
    "name": "noise",
    "type": "Basic Synth",
    "one_shot": false
  },
  {
    "id": 6,
    "name": "noise-alt",
    "type": "Basic Synth",
    "one_shot": false
  },
  {
    "id": 15,
    "name": "dwg-strings",
    "type": "DW8000",
    "one_shot": false
  },
  {
    "id": 16,
    "name": "dwg-clarinet",
    "type": "DW8000",
    "one_shot": false
  },
  {
    "id": 17,
    "name": "dwg-apiano",
    "type": "DW8000",
    "one_shot": false
  },
  {
    "id": 18,
    "name": "dwg-epiano",
    "type": "DW8000",
    "one_shot": false
  },
  {
    "id": 19,
    "name": "dwg-epiano-hard",
    "type": "DW8000",
    "one_shot": false
  },
  {
    "id": 20,
    "name": "dwg-clavi",
    "type": "DW8000",
    "one_shot": false
  },
  {
    "id": 21,
    "name": "dwg-organ",
    "type": "DW8000",
    "one_shot": false
  },
  {
    "id": 22,
    "name": "dwg-brass",
    "type": "DW8000",
    "one_shot": false
  },
  {
    "id": 23,
    "name": "dwg-sax",
    "type": "DW8000",
    "one_shot": false
  },
  {
    "id": 24,
    "name": "dwg-violin",
    "type": "DW8000",
    "one_shot": false
  },
  {
    "id": 25,
    "name": "dwg-aguitar",
    "type": "DW8000",
    "one_shot": false
  },
  {
    "id": 26,
    "name": "dwg-dguitar",
    "type": "DW8000",
    "one_shot": false
  },
  {
    "id": 27,
    "name": "dwg-ebass",
    "type": "DW8000",
    "one_shot": false
  },
  {
    "id": 28,
    "name": "dwg-dbass",
    "type": "DW8000",
    "one_shot": false
  },
  {
    "id": 29,
    "name": "dwg-bell",
    "type": "DW8000",
    "one_shot": false
  },
  {
    "id": 30,
    "name": "dwg-whistle",
    "type": "DW8000",
    "one_shot": false
  },
  {
    "id": 31,
    "name": "krg-17",
    "type": "DW8000",
    "one_shot": false
  },
  {
    "id": 32,
    "name": "krg-18",
    "type": "DW8000",
    "one_shot": false
  },
  {
    "id": 33,
    "name": "krg-19",
    "type": "DW8000",
    "one_shot": false
  },
  {
    "id": 34,
    "name": "krg-20",
    "type": "DW8000",
    "one_shot": false
  },
  {
    "id": 35,
    "name": "krg-21",
    "type": "DW8000",
    "one_shot": false
  },
  {
    "id": 36,
    "name": "krg-22",
    "type": "DW8000",
    "one_shot": false
  },
  {
    "id": 37,
    "name": "krg-23",
    "type": "DW8000",
    "one_shot": false
  },
  {
    "id": 38,
    "name": "krg-24",
    "type": "DW8000",
    "one_shot": false
  },
  {
    "id": 39,
    "name": "krg-25",
    "type": "DW8000",
    "one_shot": false
  },
  {
    "id": 40,
    "name": "krg-26",
    "type": "DW8000",
    "one_shot": false
  },
  {
    "id": 41,
    "name": "krg-27",
    "type": "DW8000",
    "one_shot": false
  },
  {
    "id": 42,
    "name": "krg-28",
    "type": "DW8000",
    "one_shot": false
  },
  {
    "id": 43,
    "name": "krg-29",
    "type": "DW8000",
    "one_shot": false
  },
  {
    "id": 44,
    "name": "krg-30",
    "type": "DW8000",
    "one_shot": false
  },
  {
    "id": 45,
    "name": "krg-31",
    "type": "DW8000",
    "one_shot": false
  },
  {
    "id": 46,
    "name": "krg-32",
    "type": "DW8000",
    "one_shot": false
  },
  {
    "id": 47,
    "name": "cosine",
    "type": "Basic Synth",
    "one_shot": false
  },
  {
    "id": 48,
    "name": "centered pulse",
    "type": "Basic Synth",
    "one_shot": false
  },
  {
    "id": 49,
    "name": "centered krg2",
    "type": "Basic Synth",
    "one_shot": false
  },
  {
    "id": 50,
    "name": "saw",
    "type": "ESQ-1",
    "one_shot": false
  },
  {
    "id": 51,
    "name": "bell",
    "type": "ESQ-1",
    "one_shot": false
  },
  {
    "id": 52,
    "name": "sine",
    "type": "ESQ-1",
    "one_shot": false
  },
  {
    "id": 53,
    "name": "square",
    "type": "ESQ-1",
    "one_shot": false
  },
  {
    "id": 54,
    "name": "pulse",
    "type": "ESQ-1",
    "one_shot": false
  },
  {
    "id": 55,
    "name": "noise1",
    "type": "ESQ-1",
    "one_shot": false
  },
  {
    "id": 56,
    "name": "noise2",
    "type": "ESQ-1",
    "one_shot": false
  },
  {
    "id": 57,
    "name": "noise3",
    "type": "ESQ-1",
    "one_shot": false
  },
  {
    "id": 58,
    "name": "bass",
    "type": "ESQ-1",
    "one_shot": false
  },
  {
    "id": 59,
    "name": "piano",
    "type": "ESQ-1",
    "one_shot": false
  },
  {
    "id": 60,
    "name": "elpno",
    "type": "ESQ-1",
    "one_shot": false
  },
  {
    "id": 61,
    "name": "voice1",
    "type": "ESQ-1",
    "one_shot": false
  },
  {
    "id": 62,
    "name": "voice2",
    "type": "ESQ-1",
    "one_shot": false
  },
  {
    "id": 63,
    "name": "kick",
    "type": "ESQ-1",
    "one_shot": true
  },
  {
    "id": 64,
    "name": "reed",
    "type": "ESQ-1",
    "one_shot": false
  },
  {
    "id": 65,
    "name": "organ",
    "type": "ESQ-1",
    "one_shot": false
  },
  {
    "id": 66,
    "name": "synth1",
    "type": "ESQ-1",
    "one_shot": false
  },
  {
    "id": 67,
    "name": "synth2",
    "type": "ESQ-1",
    "one_shot": false
  },
  {
    "id": 68,
    "name": "synth3",
    "type": "ESQ-1",
    "one_shot": false
  },
  {
    "id": 69,
    "name": "formt1",
    "type": "ESQ-1",
    "one_shot": false
  },
  {
    "id": 70,
    "name": "formt2",
    "type": "ESQ-1",
    "one_shot": false
  },
  {
    "id": 71,
    "name": "formt3",
    "type": "ESQ-1",
    "one_shot": false
  },
  {
    "id": 72,
    "name": "formt4",
    "type": "ESQ-1",
    "one_shot": false
  },
  {
    "id": 73,
    "name": "formt5",
    "type": "ESQ-1",
    "one_shot": false
  },
  {
    "id": 74,
    "name": "pulse2",
    "type": "ESQ-1",
    "one_shot": false
  },
  {
    "id": 75,
    "name": "sqr2",
    "type": "ESQ-1",
    "one_shot": false
  },
  {
    "id": 76,
    "name": "4octs",
    "type": "ESQ-1",
    "one_shot": false
  },
  {
    "id": 77,
    "name": "prime",
    "type": "ESQ-1",
    "one_shot": false
  },
  {
    "id": 78,
    "name": "brass",
    "type": "ESQ-1",
    "one_shot": false
  },
  {
    "id": 79,
    "name": "string",
    "type": "ESQ-1",
    "one_shot": false
  },
  {
    "id": 80,
    "name": "octave",
    "type": "ESQ-1",
    "one_shot": false
  },
  {
    "id": 81,
    "name": "oct5th",
    "type": "ESQ-1",
    "one_shot": false
  },
  {
    "id": 82,
    "name": "kick",
    "type": "Drum",
    "one_shot": true
  },
  {
    "id": 83,
    "name": "snare",
    "type": "Drum",
    "one_shot": true
  },
  {
    "id": 84,
    "name": "chh",
    "type": "Drum",
    "one_shot": true
  },
  {
    "id": 85,
    "name": "ohh",
    "type": "Drum",
    "one_shot": true
  },
  {
    "id": 86,
    "name": "clap",
    "type": "Drum",
    "one_shot": true
  },
  {
    "id": 87,
    "name": "rim",
    "type": "Drum",
    "one_shot": true
  },
  {
    "id": 88,
    "name": "tomlo",
    "type": "Drum",
    "one_shot": true
  },
  {
    "id": 89,
    "name": "tommid",
    "type": "Drum",
    "one_shot": true
  },
  {
    "id": 90,
    "name": "tomhi",
    "type": "Drum",
    "one_shot": true
  },
  {
    "id": 91,
    "name": "lotom",
    "type": "Drum",
    "one_shot": true
  },
  {
    "id": 92,
    "name": "midtom",
    "type": "Drum",
    "one_shot": true
  },
  {
    "id": 93,
    "name": "hitom",
    "type": "Drum",
    "one_shot": true
  },
  {
    "id": 94,
    "name": "crash",
    "type": "Drum",
    "one_shot": true
  },
  {
    "id": 95,
    "name": "cymbal",
    "type": "Drum",
    "one_shot": true
  },
  {
    "id": 96,
    "name": "cowbell",
    "type": "Drum",
    "one_shot": true
  },
  {
    "id": 97,
    "name": "clave",
    "type": "Drum",
    "one_shot": true
  },
  {
    "id": 98,
    "name": "maracas",
    "type": "Drum",
    "one_shot": true
  },
  {
    "id": 99,
    "name": "trigger",
    "type": "Drum",
    "one_shot": true
  }
];
