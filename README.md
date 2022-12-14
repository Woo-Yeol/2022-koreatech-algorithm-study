# 2022-koreatech-algorithm-study
한국기술교육대학교 17학번 알고리즘 스터디 (2022.09.01 ~ 2022.10.01)

- **From : https://github.com/woowacourse-study/2022-lv3-algorithm-study**

notion: https://wooyeol.notion.site/d4e248357172424ebd85b5ec7a624514

## 진행 시각

- `2022.09.01 ~ 2022.10.01` 제9회 프로그래밍 대회 기간까지 진행됨.
- 문제 PR 마감: `매주 토요일 08:00:00`
- 코드리뷰 마감: `매주 월요일 02:00:00`

## 진행 목표

- 어떤 방식으로 문제를 접근하고 해결하는지를 탐구해본다
- 시간과 문제 수에 구애 받지 않고 풀이해본다
- 다양한 코드들을 리뷰해주면서 수많은 풀이법을 공부하여 시야를 확장시킨다

## 진행 방법

- **매일 정해진 문제들을 한 문제 이상씩**풀이합니다.
    - 과제 문제는 주차가 진행될수록 난이도가 증가하며, 더 많은 알고리즘의 문제들이 제공됩니다.
    - 과제 난이도는 초기에는 `solvedac 기준 브론즈 중위 ~ 실버 하위 (프로그래머스 lv1)` 에서, 마무리 때에는 `solvedac 기준 골드 하위 ~ 골드 중상위 (프로그래머스 lv3)` 까지 진행될 수 있습니다.
    - **알고리즘 수업 및 토론은 공식적으로는 진행되지 않습니다.** 다만, 과제를 제출하기 위해서는 그 알고리즘에 대한 이해는 있도록 문제를 구성할 것입니다. 스스로 또는 크루들과 함께 알고리즘을 공부하고 과제를 진행합시다.
- 문제를 풀고 해당 주차에 PR을 제출합니다. 기한은 `월 ~ 토요일`입니다.
- PR을 제출한 후, 본인이 리뷰해주어야 하는 다른 PR들을 리뷰해줍니다. 기한은 `월요일 ~ 차주 월요일`입니다.

(진행 방법은 https://github.com/kth990303/BojCodingTestStudy 와 유사하게 진행되므로 참고하실 분은 들어가보시면 좋을 것 같습니다)

## 벌금

- 문제 PR을 제 시간 내에 제출하지 않은 경우: `벌금 10,000원`
- 월요일 02시 기준으로 merge가 불가능한 PR: **해당 PR 리뷰를 하지 않은 리뷰어**가 `벌금 5,000원`

## 깃허브 이용 방법

### 과제 제출방법

1. repository를 `fork` 후, `clone`합니다. (초기 1회만) / 새로운 주차 폴더가 생겼을 경우 clone이 아닌 `pull` 또는 `fetch`을 진행합니다.
2. fork한 저장소의 각 주차에 해당되는 과제 폴더에 소스 코드를 `add`, `commit` 후 `push` 합니다. 파일명은 `문제번호_언어_이름`으로 합니다. ex) `14888_cpp_김태현`
3. PR을 보낸 후, code review를 기다립니다. PR 제목은 `[이름] O일차 과제 제출 (문제 번호)`로 합니다. ex) `[케이] 2일차 과제 제출 (문제 번호)`, `[케이]O일차 과제 제출 (문제 번호)`
4. code Reviewer는 **모두** 진행합니다
5. `changes requested`일 경우 피드백 반영 후 2, 3번을 반복합니다.
6. `merged`일 경우, 다른 과제를 진행합니다.

### Git branch Protection Rule

1. `2022-koreatech-algorithm-study:main` 브랜치에는 push가 불가능합니다. PR을 보내주고 코드리뷰어들의 `approve`로 승인을 받아야 `2022-koreatech-algorithm-study:main`으로 병합됩니다.
2. 하나의 PR에는 `최소 2개 이상의 approve`가 있어야 합니다.
3. 지정된 코드리뷰어의 review는 반드시 받아야 합니다.
