#!/usr/bin/env python3
"""Generate a review copy of Prompt em Pauta episode 01 with ElevenLabs TTS.

The approved narration is read from roteiro/narracao-utilizada.txt.
Credentials are read from environment variables or a local .env file.
The script deliberately writes a separate candidate MP3 and does not overwrite
the existing eSpeak deliverable.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
ENV_FILE = ROOT / ".env"
SCRIPT_FILE = ROOT / "roteiro" / "narracao-utilizada.txt"
OUTPUT_FILE = ROOT / "output" / "episodio-01-prompt-em-pauta-elevenlabs.mp3"


def load_local_env() -> None:
    """Load simple KEY=VALUE entries from .env without overriding shell vars."""
    if not ENV_FILE.exists():
        return
    for raw_line in ENV_FILE.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def main() -> int:
    load_local_env()
    api_key = os.getenv("ELEVENLABS_API_KEY", "").strip()
    voice_id = os.getenv("ELEVENLABS_VOICE_ID", "").strip()

    if not api_key or api_key == "coloque_sua_chave_aqui":
        print("Configure ELEVENLABS_API_KEY no arquivo .env ou no ambiente.", file=sys.stderr)
        return 2
    if not voice_id or voice_id == "ID_DA_VOZ_THE_PROFESSIONAL_INSTRUCTOR":
        print(
            "Configure ELEVENLABS_VOICE_ID com o ID da voz The Professional Instructor "
            "da sua conta ElevenLabs.",
            file=sys.stderr,
        )
        return 2
    if not SCRIPT_FILE.exists():
        print(f"Roteiro não encontrado: {SCRIPT_FILE}", file=sys.stderr)
        return 2

    narration = SCRIPT_FILE.read_text(encoding="utf-8").strip()
    if not narration:
        print("O arquivo de narração está vazio.", file=sys.stderr)
        return 2
    if len(narration) > 5000:
        print(
            f"O texto tem {len(narration)} caracteres. Divida-o em blocos antes de gerar; "
            "o script foi preparado para este roteiro de até 5.000 caracteres.",
            file=sys.stderr,
        )
        return 2

    endpoint = (
        "https://api.elevenlabs.io/v1/text-to-speech/"
        f"{quote(voice_id, safe='')}?output_format=mp3_44100_128"
    )
    payload = {
        "text": narration,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.55,
            "similarity_boost": 0.78,
            "style": 0.10,
            "use_speaker_boost": True,
        },
    }
    request = Request(
        endpoint,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={
            "xi-api-key": api_key,
            "Content-Type": "application/json",
            "Accept": "audio/mpeg",
        },
        method="POST",
    )

    try:
        with urlopen(request, timeout=180) as response:
            audio_bytes = response.read()
    except HTTPError as exc:
        details = exc.read().decode("utf-8", errors="replace")
        print(f"ElevenLabs retornou HTTP {exc.code}: {details[:1200]}", file=sys.stderr)
        return 1
    except URLError as exc:
        print(f"Não foi possível conectar ao ElevenLabs: {exc.reason}", file=sys.stderr)
        return 1
    except TimeoutError:
        print("A solicitação ao ElevenLabs excedeu o tempo limite.", file=sys.stderr)
        return 1

    if not audio_bytes:
        print("A API não retornou dados de áudio.", file=sys.stderr)
        return 1

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_bytes(audio_bytes)
    print(f"Áudio candidato gerado: {OUTPUT_FILE.relative_to(ROOT)}")
    print("Ouça o MP3 integralmente antes de substituir o áudio final do projeto.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
