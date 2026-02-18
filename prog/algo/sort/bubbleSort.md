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
insertionSort(A, N)
    for(int i = 0; i < N; i++){
        v = A[i];
        j = i - 1;
        while(j >= 0 && A[j] > v){
            A[j + 1]=A[j];
            j--;
        }
        A[j+1]=v;
    }
```

{% endraw %}

*N*個の要素を含む数列*A*を昇順に並び替える挿入ソートのプログラムは以下のようになる。

{% raw %}

```c
#include <stdio.h>

void printArray(int A[], int N);

void InsertionSort(int A[], int N)
{
    for (int i = 0; i < N; i++)
    {
        int v = A[i];
        int j = i - 1;
        while (j >= 0 && A[j] > v)
        {
            A[j + 1] = A[j];
            j--;
        }
        A[j + 1] = v;

        printArray(A, N);
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

    InsertionSort(A, N);

    return 0;
}
```

{% endraw %}

---

## 最新の記事・更新

- 2026-02-08: サイトを開設しました。

---

© 2026 shunchama. Built with GitHub Pages.
