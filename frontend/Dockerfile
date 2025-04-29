# Stage 1
FROM node:20.19.1-alpine3.21 AS builder

WORKDIR /app

COPY package*.json ./

RUN npm ci --ignore-scripts --no-progress --quiet

COPY . .

RUN npm run build

# Stage 2
FROM nginx:stable-alpine

COPY nginx.conf /etc/nginx/nginx.conf

COPY --from=builder /app/dist/frontend/browser /usr/share/nginx/html/

CMD [ "nginx", "-g", "daemon off;" ]
