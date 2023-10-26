FROM gomicro/goose

#ADD *.sql /migrations/
ADD entrypoint.sh /

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]