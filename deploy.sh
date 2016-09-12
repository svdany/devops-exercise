TAGS="none"
SKIP_TAGS="common"

case $1 in
  "all")
  TAGS="all"
  ;;
  "big-service")
  TAGS="big-service"
  ;;
  "panda-service")
  TAGS="panda-service"
  ;;
esac

if [ "$TAGS" != "none" ]; then
  /usr/local/bin/ansible-playbook \
    --connection=ssh \
    --timeout=30 \
    --extra-vars=ansible_ssh_user='vagrant' \
    --limit=base \
    --inventory-file=dev \
    --extra-vars='{"ansible_connection":"ssh","ansible_ssh_args":"-o ForwardAgent=yes"}' \
    --skip-tags=$SKIP_TAGS \
    --tags=$TAGS \
  base.yml
else
  echo "Usage: $0 service_name"
  echo "accepted service_name values"
  echo "  - big-service"
  echo "  - panda-service"
  echo "  - all"
fi
