FROM ubuntu:20.04

MAINTAINER plutohiyo@gmail.com

RUN buildDeps='systemd python3 python3-pip init' \
    && apt-get update \
    && apt-get install -y $buildDeps \
    && apt-get autoremove -y \
    && apt-get autoclean -y	

COPY conf/*.service /etc/systemd/system/

RUN systemctl enable /etc/systemd/system/pythonhttp.service \
    && pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip \
    && pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade virtualenv \
    && pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade setuptools \
    && pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple aliyun-python-sdk-core-v3 \
    && pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple aliyun-python-sdk-alidns

RUN mkdir -p /var/pythonhttp/cgi-bin
COPY script/ddns.py /var/pythonhttp/cgi-bin/
RUN chmod 777 -R /var/pythonhttp

EXPOSE 18888/tcp

CMD ["/sbin/init"]

