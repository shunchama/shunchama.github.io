---
layout: default
title: 安定ソート(StableSort)
parent: アルゴリズム
nav_order: 4
date: 2026-02-19
---

# 安定ソート

トランプのカードを整列することを考える。ここで、*4*つの絵柄(S, H, C, D)と9つの数字(1, 2, ..., 9)から構成される*36*枚のカードを用いることにする。例えば、ハートの*8*は*H8*と表す。

バブルソート及び選択ソートのアルゴリズムを用いて、与えられた*N*枚のカードをそれらの数字を基準に照準に整列するプログラムの作成を目指す。

ここで、同じ数字を持つカードが複数ある場合それらが入力に出現する順序で出力されることを「安定な出力」と呼ぶ。

バブルソートは、配列要素の隣同士のみを比較・交換するので、要素のキーが同じだった場合、それらの順番が入れ替わることはない。従ってバブルソートは安定なソートです。ただし隣同士を比較する演算*A[j]<A[j-1]*に等号を入れて*A[j]<A[j-1]*としてしまうと安定ではなくなるので注意が必要である。

挿入ソートは離れた要素を直接交換することはない。挿入の位置を選ぶ過程の要素の動きは、バブルソートの原理に類似している。よって、挿入ソートは安定なソートアルゴリズムといえる。

この問題については、ソートの結果が安定かどうかを調べるには、*N*の値が小さいので、次のようなカードの組に対する順番を愚直に調べる *O(N^4)*のアルゴリズムを適用する。

**アルゴリズム**

{% raw %}

```c
int is_stable(int N, Card in_c[], Card out_c[])
{
    for (int i = 0; i < N; i++)
    {
        for (int j = i + 1; j < N; j++)
        {
            if (out_c[i].num == out_c[j].num)
            {
                int in_idx_i = -1, in_idx_j = -1;
                for (int k = 0; k < N; k++)
                {
                    if (in_c[k].num == out_c[i].num && in_c[k].mark == out_c[i].mark)
                    {
                        if (in_idx_i == -1)
                        {
                            in_idx_i = k;
                        }
                    }
                    if (in_c[k].num == out_c[j].num && in_c[k].mark == out_c[j].mark)
                    {
                        if (in_idx_j == -1 && k != in_idx_i)
                        {
                            in_idx_j = k;
                        }
                    }
                }
                if (in_idx_i > in_idx_j)
                {
                    return 0;
                }
            }
        }
    }
    return 1;
}
```

{% endraw %}

---

*N*個の要素を含む数列*A*を昇順に並び替えるプログラムは以下のようになる。

{% raw %}

```c
#include <stdio.h>

typedef struct
{
    char mark;
    int num;
} Card;

void printArray(int N, Card A[N]);
void swap_card(Card *a, Card *b);
int is_stable(int N, Card in_c[], Card out_c[]);

void bubbleSort(Card A[], int N)
{
    int flag = 1;
    while (flag)
    {
        flag = 0;
        for (int i = N - 1; i >= 1; i--)
        {
            if (A[i - 1].num > A[i].num)
            {

                swap_card(&A[i - 1], &A[i]);
                flag = 1;
            }
        }
    }
}

void selectionSort(Card A[], int N)
{
    for (int i = 0; i < N; i++)
    {
        int minj = i;
        for (int j = i; j < N; j++)
        {
            if (A[j].num < A[minj].num)
            {
                minj = j;
            }
        }
        if (i != minj)
        {

            swap_card(&A[i], &A[minj]);
        }
    }
}

int main()
{
    int N;
    scanf("%d", &N);
    Card C1[N], C2[N], org[N];

    for (int i = 0; i < N; i++)
    {
        scanf(" %c%d", &org[i].mark, &org[i].num);
        C1[i] = C2[i] = org[i];
    }

    // BubbleSort
    bubbleSort(C1, N);
    printArray(N, C1);
    printf("%s\n", is_stable(N, org, C1) ? "Stable" : "Not stable");

    // SelectionSort
    selectionSort(C2, N);
    printArray(N, C2);
    printf("%s\n", is_stable(N, org, C2) ? "Stable" : "Not stable");

    return 0;
}

void printArray(int N, Card A[N])
{
    for (int i = 0; i < N; i++)
    {
        printf("%c%d", A[i].mark, A[i].num);
        if (i < N - 1)
        {
            printf(" ");
        }
    }
    printf("\n");
}

void swap_card(Card *a, Card *b)
{
    Card tmp = *a;
    *a = *b;
    *b = tmp;
}

int is_stable(int N, Card in_c[], Card out_c[])
{
    for (int i = 0; i < N; i++)
    {
        for (int j = i + 1; j < N; j++)
        {
            if (out_c[i].num == out_c[j].num)
            {
                int in_idx_i = -1, in_idx_j = -1;
                for (int k = 0; k < N; k++)
                {
                    if (in_c[k].num == out_c[i].num && in_c[k].mark == out_c[i].mark)
                    {
                        if (in_idx_i == -1)
                        {
                            in_idx_i = k;
                        }
                    }
                    if (in_c[k].num == out_c[j].num && in_c[k].mark == out_c[j].mark)
                    {
                        if (in_idx_j == -1 && k != in_idx_i)
                        {
                            in_idx_j = k;
                        }
                    }
                }
                if (in_idx_i > in_idx_j)
                {
                    return 0;
                }
            }
        }
    }
    return 1;
}

```

{% endraw %}

---

## 最新の記事・更新

- 2026-02-08: サイトを開設しました。

---

© 2026 shunchama. Built with GitHub Pages.
