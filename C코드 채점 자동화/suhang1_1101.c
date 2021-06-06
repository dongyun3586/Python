#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main() {
	int random1, ans;
	int time1;
	printf("*** 1학년 1반 1번 강예혁 ***\n 1부터 100사이 숫자를 추측하는 게입입니다.");
	srand(time(NULL));
	random1 = rand()%100 + 1;
	printf("\n정답은: %d\n", random1);
	for (int i = 1; ; i++) {
		printf("정답은?: ");
		scanf_s("%d", &ans);
		if (ans > random1) {
			printf("\n 틀렸습니다, %d보다 작습니다\n", ans);
		}
		else if (ans < random1) {
			printf("틀려습니다, %d보다 큽니다\n", ans);
		}
		else {
			time1 = i;
			printf("정답입니다.\n");
			break;
		}
		
	}
	printf("%d번 만에 맟췄습니다.", time1);
}