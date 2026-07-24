# Git & GitHub 핵심 요약

**Git이란?** 파일 변경 이력을 기록·관리하는 버전 관리 도구 (내 컴퓨터에서 동작)
**GitHub란?** Git 저장소를 올려 공유·협업하는 웹 서비스

---

## 기본 개념

- **Repository**: 프로젝트 + 변경 이력이 담긴 저장소
- **Commit**: 변경 사항을 기록하는 단위 (버전 하나)
- **Branch**: 독립적으로 작업하는 공간, 끝나면 merge
- **HEAD**: 현재 작업 위치를 가리키는 포인터
- **Working Directory → Staging Area → Repository**: `git add`로 스테이징, `git commit`으로 저장

---

## 핵심 명령어

```
git init                     # 저장소 초기화
git status                   # 상태 확인
git add .                    # 스테이징
git commit -m "메시지"        # 커밋
git branch / git switch      # 브랜치 생성/전환
git merge feature/ui         # 병합
git remote add origin URL    # 원격 연결
git push / git pull          # 원격 동기화
git clone URL                # 저장소 복사
```

---

## 협업 흐름

1. Fork(내 계정으로 복사) 또는 Clone(팀 저장소 복사)
2. 브랜치 생성 → 작업 → 커밋
3. `git push`로 원격에 업로드
4. GitHub에서 **Pull Request** 생성 → 코드 리뷰 → 병합
5. **Issue**로 할 일/버그 관리

---

## 문제 발생 시

- **Merge conflict**: 같은 부분을 다르게 수정 → 직접 수정 후 재커밋
- **git stash**: 작업 임시 저장
- **git reset**: 히스토리 되돌리기 (변경됨, 주의)
- **git revert**: 안전하게 되돌리는 새 커밋 생성 (히스토리 보존)
