---
layout: default
title: ファイル操作
parent: C言語
nav_order: 1
has_children: true
---

# ファイル操作

**fopen関数のモード文字列**

| モード文字列 | 目的                                               |
| :----------- | :------------------------------------------------- |
| **r**        | 読み込み。ファイルがない時は失敗。                 |
| **r+**       | 読み書き。ファイルがない時は失敗。                 |
| **w**        | 書き込み。ファイルがあっても空のファイルを作る。 |
| **w+**       | 読み書き。ファイルがあっても空のファイルを作る。 |
| **a**        | 追加書き込み。ファイルがない時は作る。             |
| **a+**       | 読み書き。ファイルがない時は作る。                 |

## ファイル読み込み

**read-test.txt**

```
test123file
```

**file-read.c**

```c
#include <stdio.h>
#include <stdlib.h> // require for exit()

int main()
{
    FILE *file;
    int i = 0;
    char s[100] = {0};

    // open the file for reading
    file = fopen("read-test.txt", "r");

    if (file == NULL)
    {
        fprintf(stderr, "Error: could not open file 'read-test.txt'.\n");
        return 1;
    }

    if (fscanf(file, "test%d", &i) != 1)
    {
        fprintf(stderr, "Error: failed to read an integer from the file.\n");
    }

    if (fscanf(file, "%s", s) != 1)
    {
        fprintf(stderr, "Error: failed to read an string from the file.\n");
    }

    fclose(file);

    printf("integer: %d\n", i);
    printf("string: %s\n", s);

    return 0;
}
```

**実行結果**

```
integer: 123
string: file
```

## ファイル書き込み

**file-write.c**

```c
#include <stdio.h>
#include <stdlib.h> // require for exit()

int main()
{
    FILE *file;
    int i = 123;

    // open the file for reading
    file = fopen("write-test.txt", "w");

    if (file == NULL)
    {
        fprintf(stderr, "Error: could not open file 'write-test.txt'.\n");
        return 1;
    }

    if (fprintf(file, "test%d", i) < 0) // fprintf: returns the total number of characters successfully written.
    {
        fprintf(stderr, "Error: failed to read an integer from the file.\n");
    }

    fclose(file);

    return 0;
}
```

**write-test.txt**

```
test123
```

---

## 最新の記事・更新

- 2026-02-08: サイトを開設しました。

---

© 2026 shunchama. Built with GitHub Pages.
