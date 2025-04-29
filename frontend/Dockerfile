FROM node:20.19.1-alpine3.21

WORKDIR /app

COPY package*.json ./

RUN npm ci --ignore-scripts --no-progress --quiet

COPY . .

RUN npm run build

CMD ["npm", "start", "--host", "0.0.0.0"]
