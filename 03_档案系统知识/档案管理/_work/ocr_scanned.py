# -*- coding: utf-8 -*-
"""OCR the two scanned PDFs page by page into 00-原文提取/*_OCR.txt."""
import fitz
import numpy as np
from pathlib import Path
from rapidocr import RapidOCR

SRC_DIR = Path(r'F:\ymy\公司文档\档案相关文档')
OUT_DIR = Path(r'C:\Users\DELL\Documents\ChatGPT\档案管理\00-原文提取')
TARGETS = [
    'DAT 46 文书类电子文件元数据方案.pdf',
    'GBT-18894 电子文件归档与电子档案管理.pdf',
]
ZOOM = 200 / 72


def ocr_pdf(path: Path, engine, out_path: Path):
    doc = fitz.open(str(path))
    parts = []
    for i, page in enumerate(doc):
        pix = page.get_pixmap(matrix=fitz.Matrix(ZOOM, ZOOM))
        img = np.asarray(pix.pil_image())
        res = engine(img)
        txts = list(res.txts) if res.txts else []
        parts.append(f'===== 第 {i+1} 页 =====\n' + '\n'.join(txts))
        print(f'{path.name} 第 {i+1}/{doc.page_count} 页: {len(txts)} 行', flush=True)
    out_path.write_text('\n\n'.join(parts), encoding='utf-8-sig')


def main():
    engine = RapidOCR()
    for name in TARGETS:
        src = SRC_DIR / name
        out = OUT_DIR / (src.stem + '_OCR.txt')
        print(f'--- {name} ---')
        ocr_pdf(src, engine, out)
    print('OCR DONE')


if __name__ == '__main__':
    main()
