# Etapa 1: build do frontend
FROM node:20 AS build

WORKDIR /app
COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

# Etapa 2: servidor NGINX para servir os arquivos estáticos
FROM nginx:stable-alpine
COPY --from=build /app/dist /usr/share/nginx/html

# Expõe a porta padrão do NGINX
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
