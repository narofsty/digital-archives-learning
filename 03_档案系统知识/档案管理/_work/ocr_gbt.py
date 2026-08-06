# -*- coding: utf-8 -*-
"""OCR GB_T_39362_2020 (mangled text layer) for a clean copy."""
import fitz
import numpy as np
from pathlib import Path
from rapidocr import RapidOCR

SRC = Path(r'F:\ymy\公司文档\档案相关文档\GB_T_39362_2020 党政机关电子公文归档规范.pdf')
OUT = Path(r'C:\Users\DELL\Documents\ChatGPT\档案管理\00-原文提取\GB_T_39362_2020 党政机关电子公文归档规范_OCR.txt')
ZOOM = 200 / 72


def main():
    engine = RapidOCR()
    doc = fitz.open(str(SRC))
    parts = []
    for i, page in enumerate(doc):
        pix = page.get_pixmap(matrix=fitz.Matrix(ZOOM, ZOOM))
        img = np.asarray(pix.pil_image())
        res = engine(img)
        txts = list(res.txts) if res.txts else []
        parts.append(f'===== 第 {i+1} 页 =====\n' + '\n'.join(txts))
        print(f'{SRC.name} 第 {i+1}/{doc.page_count} 页: {len(txts)} 行', flush=True)
    OUT.write_text('\n\n'.join(parts), encoding='utf-8-sig')
    print('GB_T OCR DONE')


if __name__ == '__main__':
    main()
