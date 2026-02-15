---
layout: default
title: ファイル操作
parent: リファレンス
nav_order: 1
has_children: true
---

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

---
## 最新の記事・更新
- 2026-02-08: サイトを開設しました。
  
---

© 2026 shunchama. Built with GitHub Pages.