#include <queue>
#include <cstdio>

int main() {
    int n;
    scanf("%d", &n);

    std::priority_queue<int> q;
    int total;
    for (int i = 0; i<n;i++){
        int tmp;
        scanf("%d", &tmp);
        q.push(-tmp);
    }
    while (!q.empty()){
        int a = -q.top();
        q.pop();
        int b = -q.top();
        q.pop();
        int c = (a + b) % 1000000007;
        total = (total + c) % 1000000007;
        q.push(-c);
    }
    printf("%d", total);
}
