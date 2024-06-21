FROM node:16-alpine as builder
WORKDIR '/app'
COPY . .
RUN npm install
EXPOSE 3000
CMD ["npm", "start"]