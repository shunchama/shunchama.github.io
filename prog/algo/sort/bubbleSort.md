---
layout: default
title: バブルソート(BubbleSort)
parent: アルゴリズム
nav_order: 2
date: 2026-02-18
---

# バブルソート

バブルソートはその名前が表すように、あわ(Bubble)が水面に上がっていくように配列の要素が動いていく。

**アルゴリズム**

{% raw %}

```c
void bubbleSort(int A[], int N)
{
    int flag = 1;
    while (flag)
    {
        flag = 0;
        for (int i = N - 1; i >= 1; i--)
        {
            if (A[i - 1] > A[i])
            {
                swap_cnt++;
                int tmp = A[i];
                A[i] = A[i - 1];
                A[i - 1] = tmp;
                flag = 1;
            }
        }
    }
}
```

{% endraw %}

*N*個の要素を含む数列*A*を昇順に並び替える挿入ソートのプログラムは以下のようになる。

{% raw %}

```c
#include <stdio.h>

int swap_cnt = 0;

void printArray(int A[], int N);

void bubbleSort(int A[], int N)
{
    int flag = 1;
    while (flag)
    {
        flag = 0;
        for (int i = N - 1; i >= 1; i--)
        {
            if (A[i - 1] > A[i])
            {
                swap_cnt++;
                int tmp = A[i];
                A[i] = A[i - 1];
                A[i - 1] = tmp;
                flag = 1;
            }
        }
    }
}

void printArray(int A[], int N)
{
    for (int i = 0; i < N; i++)
    {
        printf("%d", A[i]);
        if (i < N - 1)
        {
            printf(" ");
        }
    }
    printf("\n");
}

int main()
{
    int N;
    scanf("%d", &N);
    int A[N];
    for (int i = 0; i < N; i++)
    {
        scanf("%d", &A[i]);
    }

    bubbleSort(A, N);
    printArray(A, N);
    printf("%d\n", swap_cnt);

    return 0;
}
```

{% endraw %}

---

## 最新の記事・更新

- 2026-02-08: サイトを開設しました。

---

© 2026 shunchama. Built with GitHub Pages.
