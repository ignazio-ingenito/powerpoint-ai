#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TXT Novigo Document Intelligence Core
Asset downloader / packager per ricostruzione manuale PowerPoint.

Uso:
  python download_ppt_assets.py

Opzionale, se hai già scaricato le 14 immagini PNG delle slide:
  python download_ppt_assets.py --slide-dir ./slide_png

Output:
  txt_novigo_ppt_assets/
    icons/svg/
    images/slides/
    graphics/svg/
    specs/
    manifest/
"""

from __future__ import annotations

import argparse
import csv
import json
import shutil
import sys
import urllib.request
from pathlib import Path


ROOT = Path("txt_novigo_ppt_assets")

LUCIDE_BASE_URLS = [
    "https://raw.githubusercontent.com/lucide-icons/lucide/main/icons/{name}.svg",
    "https://unpkg.com/lucide-static@latest/icons/{name}.svg",
]

PALETTE = {
    "background_primary": {"hex": "#FFFFFF", "rgb": [255, 255, 255]},
    "background_secondary_1": {"hex": "#F7F7F7", "rgb": [247, 247, 247]},
    "background_secondary_2": {"hex": "#F3F6F7", "rgb": [243, 246, 247]},
    "background_secondary_3": {"hex": "#EBEFF5", "rgb": [235, 239, 245]},
    "text_primary": {"hex": "#050505", "rgb": [5, 5, 5]},
    "text_secondary": {"hex": "#5F5F5F", "rgb": [95, 95, 95]},
    "line_neutral": {"hex": "#A7A7A7", "rgb": [167, 167, 167]},
    "accent_teal": {"hex": "#52AB9F", "rgb": [82, 171, 159]},
    "accent_teal_dark": {"hex": "#4FA7A8", "rgb": [79, 167, 168]},
    "accent_blue": {"hex": "#368BD6", "rgb": [54, 139, 214]},
    "accent_blue_alt": {"hex": "#307FE2", "rgb": [48, 127, 226]},
    "accent_light_blue": {"hex": "#9FCCDB", "rgb": [159, 204, 219]},
}

FONT_SPEC = {
    "primary": "Poppins",
    "fallback": "Aptos, Arial, Helvetica, sans-serif",
    "weights": {"title": "700", "subtitle": "600", "body": "400", "caption": "400"},
    "note": "Non include file font. Installare Poppins localmente oppure usare fallback PowerPoint.",
}

SLIDE_SPECS = {
    "format": "16:9 widescreen",
    "size_px_reference": "1792 x 1024",
    "ppt_size_in": "13.333 x 7.5",
    "safe_margins": {
        "left": "0.45 in",
        "right": "0.45 in",
        "top": "0.30 in",
        "bottom": "0.30 in",
    },
    "recurring_elements": {
        "logo": "top-left, TXT | NOVIGO wordmark ricostruibile come testo",
        "slide_number": "bottom-left, teal/blue",
        "bottom_rule": "thin line, teal or blue",
        "accent_waves": "light teal/blue SVG lines, optional on cover and section slides",
    },
    "rebuild_notes": {
        "powerpoint_objects": [
            "testi",
            "card",
            "linee",
            "frecce",
            "tabelle",
            "Gantt",
            "roadmap",
            "checklist",
            "matrici",
            "icone SVG",
        ],
        "raster_or_reference": [
            "render 3D/isometrici generati",
            "eventuali slide PNG finali se usate come background di riferimento",
        ],
    },
}

ICON_MAP = {
    "common": [
        "file-text",
        "files",
        "file-search",
        "file-check",
        "file-warning",
        "folder",
        "folder-check",
        "database",
        "server",
        "cloud-upload",
        "search",
        "shield-check",
        "shield-alert",
        "calendar",
        "calendar-check",
        "check-circle",
        "x-circle",
        "help-circle",
        "alert-triangle",
        "bar-chart-3",
        "line-chart",
        "pie-chart",
        "gauge",
        "target",
        "brain-circuit",
        "cpu",
        "bot",
        "workflow",
        "git-branch",
        "settings",
        "sliders-horizontal",
        "code-2",
        "braces",
        "users",
        "user-check",
        "building-2",
        "landmark",
        "hard-hat",
        "clipboard-check",
        "clipboard-list",
        "list-checks",
        "lock",
        "key-round",
        "eye",
        "activity",
        "rocket",
        "package-check",
        "boxes",
        "layers",
        "network",
        "scan-text",
        "book-open-check",
        "scale",
        "badge-check",
        "info",
    ],
    "slide_01": [
        "boxes",
        "brain-circuit",
        "files",
        "database",
        "workflow",
        "shield-check",
    ],
    "slide_02": ["files", "puzzle", "search", "shield-alert", "database"],
    "slide_03": [
        "cloud-upload",
        "file-text",
        "scan-text",
        "folder-check",
        "calendar-check",
        "shield-check",
        "help-circle",
        "database",
        "bar-chart-3",
    ],
    "slide_04": [
        "file-text",
        "scan-text",
        "book-open-check",
        "calendar",
        "shield-check",
        "database",
    ],
    "slide_05": [
        "file-text",
        "brain-circuit",
        "shield-check",
        "clipboard-check",
        "scale",
    ],
    "slide_06": ["clipboard-list", "bar-chart-3", "check-circle", "info"],
    "slide_07": ["alert-triangle", "target"],
    "slide_08": ["file-text", "calendar", "database", "bar-chart-3", "folder-check"],
    "slide_09": [
        "hard-hat",
        "landmark",
        "folder",
        "shield-check",
        "user-check",
        "clipboard-check",
        "calendar-check",
        "workflow",
    ],
    "slide_10": [
        "clipboard-check",
        "file-check",
        "bar-chart-3",
        "shield-check",
        "briefcase",
        "check-circle",
    ],
    "slide_11": [
        "search",
        "settings",
        "line-chart",
        "rocket",
        "package-check",
        "users",
    ],
    "slide_12": [
        "brain-circuit",
        "code-2",
        "database",
        "cloud",
        "users",
        "lock",
        "eye",
        "badge-check",
        "scale",
    ],
    "slide_13": [
        "gauge",
        "shield-check",
        "boxes",
        "line-chart",
        "clipboard-list",
        "clock",
        "target",
        "brain-circuit",
    ],
    "slide_14": [
        "check-circle",
        "target",
        "shield-check",
        "bar-chart-3",
        "users",
        "file-text",
    ],
}

SLIDE_IMAGE_NAMES = [
    "01_txt_novigo_document_intelligence_core.png",
    "02_contesto_e_bisogno_operativo.png",
    "03_cosa_fa_oggi_la_poc.png",
    "04_pipeline_poc.png",
    "05_final_decision_auditabile.png",
    "06_output_poc_baseline.png",
    "07_limiti_attuali_rd.png",
    "08_evoluzione_possibile.png",
    "09_casi_uso_candidati.png",
    "10_roadmap_evolutiva.png",
    "11_macropiano_attuativo.png",
    "12_competenze_tecnologia.png",
    "13_economics_driver_decisionali.png",
    "14_decisioni_richieste.png",
]


def ensure_dirs() -> None:
    for path in [
        ROOT,
        ROOT / "icons" / "svg",
        ROOT / "images" / "slides",
        ROOT / "graphics" / "svg",
        ROOT / "specs",
        ROOT / "manifest",
    ]:
        path.mkdir(parents=True, exist_ok=True)


def download_file(url: str, dest: Path, timeout: int = 20) -> bool:
    try:
        request = urllib.request.Request(
            url, headers={"User-Agent": "Mozilla/5.0 asset-downloader"}
        )
        with urllib.request.urlopen(request, timeout=timeout) as response:
            data = response.read()
        dest.write_bytes(data)
        return True
    except Exception:
        return False


def download_lucide_icon(name: str, dest: Path) -> bool:
    for template in LUCIDE_BASE_URLS:
        url = template.format(name=name)
        if download_file(url, dest):
            return True
    return False


def create_fallback_icon(name: str, dest: Path) -> None:
    label = name[:2].upper()
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64" fill="none">
  <rect x="8" y="8" width="48" height="48" rx="10" stroke="#52AB9F" stroke-width="3"/>
  <text x="32" y="38" text-anchor="middle" font-family="Arial, sans-serif" font-size="16" font-weight="700" fill="#368BD6">{label}</text>
</svg>
"""
    dest.write_text(svg, encoding="utf-8")


def download_icons() -> list[dict]:
    all_icons = sorted({icon for icons in ICON_MAP.values() for icon in icons})
    manifest_rows = []

    print(f"Downloading {len(all_icons)} SVG icons...")

    for icon in all_icons:
        dest = ROOT / "icons" / "svg" / f"{icon}.svg"
        ok = download_lucide_icon(icon, dest)

        if not ok:
            create_fallback_icon(icon, dest)

        manifest_rows.append(
            {
                "type": "icon_svg",
                "name": icon,
                "path": str(dest),
                "source": "Lucide icons via GitHub/unpkg; fallback generated if unavailable",
                "ppt_usage": "Insert > Pictures > SVG, recolor via Graphics Format",
            }
        )

    return manifest_rows


def copy_slide_images(slide_dir: Path | None) -> list[dict]:
    rows = []
    if not slide_dir:
        return rows

    if not slide_dir.exists():
        print(f"Slide directory not found: {slide_dir}", file=sys.stderr)
        return rows

    source_images = sorted(
        list(slide_dir.glob("*.png"))
        + list(slide_dir.glob("*.jpg"))
        + list(slide_dir.glob("*.jpeg"))
    )

    for idx, source in enumerate(source_images[:14], start=1):
        dest_name = SLIDE_IMAGE_NAMES[idx - 1]
        dest = ROOT / "images" / "slides" / dest_name
        shutil.copy2(source, dest)
        rows.append(
            {
                "type": "slide_png_reference",
                "name": dest_name,
                "path": str(dest),
                "source": str(source),
                "ppt_usage": "Reference raster: use as background or visual guide; recreate elements with PPT objects where needed",
            }
        )

    return rows


def write_svg_support_graphics() -> list[dict]:
    rows = []

    wave_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="240" viewBox="0 0 1600 240" fill="none">
  <path d="M0 140 C220 40 390 220 620 120 C850 20 1040 210 1280 110 C1410 55 1510 65 1600 90" stroke="#52AB9F" stroke-width="2" opacity="0.55"/>
  <path d="M0 160 C250 60 410 235 650 135 C880 45 1040 230 1300 130 C1430 85 1510 82 1600 110" stroke="#368BD6" stroke-width="2" opacity="0.35"/>
  <path d="M0 180 C240 85 430 245 680 150 C910 60 1070 240 1320 150 C1450 105 1520 98 1600 130" stroke="#9FCCDB" stroke-width="2" opacity="0.35"/>
</svg>
"""
    wave_path = ROOT / "graphics" / "svg" / "accent_waves_teal_blue.svg"
    wave_path.write_text(wave_svg, encoding="utf-8")
    rows.append(
        {
            "type": "support_svg",
            "name": "accent_waves_teal_blue.svg",
            "path": str(wave_path),
            "source": "generated",
            "ppt_usage": "Decorative light accent waves, place bottom/right with transparency",
        }
    )

    core_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="800" height="520" viewBox="0 0 800 520" fill="none">
  <rect x="210" y="320" width="380" height="92" rx="28" fill="#EBEFF5" stroke="#9FCCDB"/>
  <rect x="235" y="250" width="330" height="92" rx="28" fill="#F3F6F7" stroke="#9FCCDB"/>
  <rect x="260" y="180" width="280" height="92" rx="28" fill="#FFFFFF" stroke="#52AB9F"/>
  <circle cx="400" cy="155" r="72" fill="url(#g1)" stroke="#52AB9F" stroke-width="2"/>
  <text x="400" y="150" text-anchor="middle" font-family="Arial, sans-serif" font-size="34" font-weight="700" fill="#FFFFFF">AI</text>
  <text x="400" y="190" text-anchor="middle" font-family="Arial, sans-serif" font-size="20" font-weight="700" fill="#FFFFFF">CORE</text>
  <text x="400" y="225" text-anchor="middle" font-family="Arial, sans-serif" font-size="20" font-weight="700" fill="#0B6F78">INTELLIGENCE LAYER</text>
  <text x="400" y="295" text-anchor="middle" font-family="Arial, sans-serif" font-size="20" font-weight="700" fill="#0B6F78">PROCESS &amp; ORCHESTRATION</text>
  <text x="400" y="365" text-anchor="middle" font-family="Arial, sans-serif" font-size="20" font-weight="700" fill="#307FE2">DATA FOUNDATION</text>
  <defs>
    <linearGradient id="g1" x1="328" y1="83" x2="472" y2="227" gradientUnits="userSpaceOnUse">
      <stop stop-color="#52AB9F"/>
      <stop offset="1" stop-color="#368BD6"/>
    </linearGradient>
  </defs>
</svg>
"""
    core_path = ROOT / "graphics" / "svg" / "document_intelligence_core_stack.svg"
    core_path.write_text(core_svg, encoding="utf-8")
    rows.append(
        {
            "type": "support_svg",
            "name": "document_intelligence_core_stack.svg",
            "path": str(core_path),
            "source": "generated",
            "ppt_usage": "Central core illustration; editable as SVG after ungrouping in PowerPoint",
        }
    )

    target_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="620" height="420" viewBox="0 0 620 420" fill="none">
  <circle cx="310" cy="190" r="150" fill="#F3F6F7"/>
  <circle cx="310" cy="190" r="120" fill="#52AB9F" opacity="0.22"/>
  <circle cx="310" cy="190" r="88" fill="#FFFFFF" stroke="#52AB9F" stroke-width="18"/>
  <circle cx="310" cy="190" r="48" fill="#52AB9F" opacity="0.85"/>
  <path d="M310 190 L460 78" stroke="#0B6F78" stroke-width="14" stroke-linecap="round"/>
  <path d="M440 54 L500 70 L468 116 Z" fill="#368BD6"/>
  <text x="310" y="385" text-anchor="middle" font-family="Arial, sans-serif" font-size="24" font-weight="700" fill="#0B6F78">BUSINESS IMPACT</text>
</svg>
"""
    target_path = ROOT / "graphics" / "svg" / "business_impact_target.svg"
    target_path.write_text(target_svg, encoding="utf-8")
    rows.append(
        {
            "type": "support_svg",
            "name": "business_impact_target.svg",
            "path": str(target_path),
            "source": "generated",
            "ppt_usage": "Final decision board / closing visual",
        }
    )

    return rows


def write_specs() -> None:
    (ROOT / "specs" / "palette.json").write_text(
        json.dumps(PALETTE, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    (ROOT / "specs" / "font_spec.json").write_text(
        json.dumps(FONT_SPEC, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    (ROOT / "specs" / "layout_spec.json").write_text(
        json.dumps(SLIDE_SPECS, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    readme = """# TXT Novigo Document Intelligence Core — PowerPoint Asset Pack

## Uso in PowerPoint

1. Inserire le icone SVG da `icons/svg/`.
2. Usare la palette in `specs/palette.json`.
3. Ricostruire testi, card, frecce, tabelle e Gantt come oggetti PowerPoint.
4. Usare gli SVG in `graphics/svg/` come elementi illustrativi o come base da modificare.
5. Se disponibili, usare le immagini in `images/slides/` come riferimento raster o come background temporaneo.

## Font

Font consigliato: Poppins.
Fallback: Aptos / Arial / Helvetica.

Questo pacchetto non include file font.

## Colori principali

- Bianco: #FFFFFF
- Testo primario: #050505
- Testo secondario: #5F5F5F
- Teal: #52AB9F
- Teal scuro: #4FA7A8
- Azzurro: #368BD6 / #307FE2
- Azzurro chiaro: #9FCCDB
- Grigi leggeri: #F7F7F7 / #F3F6F7 / #EBEFF5

## Elementi ricostruibili come oggetti PowerPoint

- card e bordi;
- linee e frecce;
- pipeline numerata;
- matrice limiti;
- roadmap;
- Gantt macro;
- capability wheel;
- checklist finale;
- icone SVG.

## Elementi che possono restare raster

- render 3D/isometrici generati;
- eventuali immagini PNG finali delle slide.
"""
    (ROOT / "README.md").write_text(readme, encoding="utf-8")


def write_manifest(rows: list[dict]) -> None:
    csv_path = ROOT / "manifest" / "asset_manifest.csv"
    fieldnames = ["type", "name", "path", "source", "ppt_usage"]

    with csv_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    json_path = ROOT / "manifest" / "asset_manifest.json"
    json_path.write_text(
        json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--slide-dir",
        type=Path,
        default=None,
        help="Cartella locale contenente le 14 immagini PNG/JPG delle slide già scaricate.",
    )
    args = parser.parse_args()

    ensure_dirs()

    manifest_rows = []
    manifest_rows.extend(download_icons())
    manifest_rows.extend(write_svg_support_graphics())
    manifest_rows.extend(copy_slide_images(args.slide_dir))

    write_specs()
    write_manifest(manifest_rows)

    print()
    print("Asset pack creato:")
    print(f"  {ROOT.resolve()}")
    print()
    print("Cartelle principali:")
    print(f"  Icons SVG:      {(ROOT / 'icons' / 'svg').resolve()}")
    print(f"  Graphics SVG:   {(ROOT / 'graphics' / 'svg').resolve()}")
    print(f"  Specs:          {(ROOT / 'specs').resolve()}")
    print(f"  Manifest:       {(ROOT / 'manifest').resolve()}")
    print()
    if args.slide_dir:
        print(f"Slide raster copiate da: {args.slide_dir.resolve()}")
    else:
        print(
            "Nota: per includere anche le immagini PNG delle 14 slide, scaricale in una cartella e rilancia:"
        )
        print("  python download_ppt_assets.py --slide-dir ./slide_png")


if __name__ == "__main__":
    main()
