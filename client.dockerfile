FROM node:lts-alpine as setup-stage
WORKDIR /app
COPY client/shipments_client/package*.json ./
RUN npm install
COPY client/shipments_client/ .

FROM setup-stage as build-stage
RUN npm run build

FROM nginx:stable-alpine as dev-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]