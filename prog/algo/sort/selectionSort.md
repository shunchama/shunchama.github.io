---
layout: default
title: 選択ソート(SelectionSort)
parent: アルゴリズム
nav_order: 3
date: 2026-02-19
---

# 選択ソート

選択ソートは各計算ステップで1つの最小値を選択していくアルゴリズムである。

**アルゴリズム**

{% raw %}

```c
void selectionSort(int A[], int N)
{
    for (int i = 0; i < N; i++)
    {
        int minj = i;
        for (int j = i; j < N; j++)
        {
            if (A[j] < A[minj])
            {
                minj = j;
            }
        }
        if (A[i] > A[minj])
        {
            swap_cnt++;
            swap(&A[i], &A[minj]);
        }
    }
}
```

{% endraw %}

*N*個の要素を含む数列*A*を昇順に並び替える選択ソートのプログラムは以下のようになる。

{% raw %}

```c
#include <stdio.h>

int swap_cnt = 0;

void printArray(int A[], int N);

void swap(int *a, int *b);

void selectionSort(int A[], int N)
{
    for (int i = 0; i < N; i++)
    {
        int minj = i;
        for (int j = i; j < N; j++)
        {
            if (A[j] < A[minj])
            {
                minj = j;
            }
        }
        if (A[i] > A[minj])
        {
            swap_cnt++;
            swap(&A[i], &A[minj]);
        }
    }
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

    selectionSort(A, N);
    printArray(A, N);
    printf("%d\n", swap_cnt);

    return 0;
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

void swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}
```

{% endraw %}

---

## 最新の記事・更新

- 2026-02-08: サイトを開設しました。

---

© 2026 shunchama. Built with GitHub Pages.
