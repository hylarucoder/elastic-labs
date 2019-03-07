ARG ELK_VERSION

FROM elastic/filebeat:${ELK_VERSION}

# Add your kibana plugins setup here
RUN filebeat modules enable system nginx mysql
