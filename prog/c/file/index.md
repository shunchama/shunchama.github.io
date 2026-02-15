---
layout: default
title: ファイル操作
parent: リファレンス
nav_order: 1
has_children: true
---

# ファイル操作

## ファイル読み込み

**read-test.txt**

```
test123file
```


**file-read**

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

**file-write**

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

---

## 最新の記事・更新

- 2026-02-08: サイトを開設しました。

---

© 2026 shunchama. Built with GitHub Pages.
