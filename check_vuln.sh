#!/bin/bash

echo "=== 보안 점검 결과 ==="

# [U-15] 소유자 없는 파일 찾기 (시스템 폴더 제외)
echo -e "\n[U-15 점검] 소유자 없는 파일 목록:"
find / \( -path /proc -o -path /sys -o -path /dev -o -path /run \) -prune -o -nouser -ls 2>/dev/null

# [U-25] World Writable 파일 찾기 (시스템 폴더 제외)
echo -e "\n[U-25 점검] World Writable 파일 목록:"
find / \( -path /proc -o -path /sys -o -path /dev -o -path /run \) -prune -o -type f -perm -0002 -ls 2>/dev/null

echo -e "\n=== 점검 완료 ==="
