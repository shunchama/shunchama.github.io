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

*N*個の要素を含む数列*A*を昇順に並び替えるバブルソートのプログラムは以下のようになる。

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
