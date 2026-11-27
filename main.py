import os

# Snap the Beans: one quiet act of thanks, written out as plain text.
# Standard library only; no network, no randomness.

TEXT = "Thank you. At dusk I walk down the bean rows and pick green beans for your supper, cool pods, one by one, off the vine. I snap them into the bowl, pod after pod, the ends falling soft, till the bowl fills green. Eat them warm with butter. The snap stays in my hands, green and fresh, long after supper is done."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        # The output is exactly TEXT, byte for byte.
        f.write(TEXT)

if __name__ == "__main__":
    main()
