---
layout: default
title: 挿入ソート(InsertionSort)
parent: アルゴリズム
nav_order: 1
date: 2026-02-18
---

# 挿入ソート

挿入ソートは手持ちのトランプを並び替えるときに使われる、自然で思いつきやすいアルゴリズムの1つである。片手に持ったトランプを左から小さい順に並び替える場合、1枚ずつカードを取り出して、それをその時点ですでにソートされている並びの適切な位置に挿入していくことによって、カードを並び替えることができる。
プログラム中の while (j >= 0 && A[j] > v) という部分は、「左側にずらしながら挿入場所を探す」作業をしている。

**アルゴリズム**

{% raw %}

```c
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
```

{% endraw %}

---

*N*個の要素を含む数列*A*を昇順に並び替えるバブルソートのプログラムは以下のようになる。

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
