set -x

cat > "${ROOTDIR}/README.md" <<- EOF
	$(git -C "ROOTDIR" log --format='%N <%aE>' | LC_ALL=C.UTF-8 sort -uf)
EOF
