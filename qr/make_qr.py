"""Make a print-quality QR code PNG for a link.

    pip install "qrcode[pil]"
    python3 make_qr.py https://suffolklitsa.org/rsvp rsvp-qr.png
"""
import sys

import qrcode


def main(url: str, out: str, box: int = 20) -> None:
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=box, border=2)
    qr.add_data(url)
    qr.make(fit=True)
    qr.make_image(fill_color="black", back_color="white").save(out)
    print(f"wrote {out} for {url}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("usage: make_qr.py URL OUTPUT.png")
    main(sys.argv[1], sys.argv[2])
