ln -s ~/Code/MCB185/data/dictionary.gz dic.gz
gunzip -c dic.gz | grep -E ".{4,}" | grep -v "[^zonrcai]" | grep -c "[r]"