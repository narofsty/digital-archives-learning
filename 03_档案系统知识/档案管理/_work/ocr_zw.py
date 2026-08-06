# -*- coding: utf-8 -*-
"""OCR GB/T 42727-2023 (garbled text layer)."""
import fitz
import numpy as np
from pathlib import Path
from rapidocr import RapidOCR

SRC = Path(r'F:\ymy\公司文档\档案相关文档\政务服务事项电子文件归档规范GBT+42727-2023.pdf')
OUT = Path(r'C:\Users\DELL\Documents\ChatGPT\档案管理\00-原文提取\政务服务事项电子文件归档规范GBT+42727-2023_OCR.txt')
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
    print('GB/T 42727 OCR DONE')


if __name__ == '__main__':
    main()
