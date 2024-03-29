FROM node:18-alpine AS builder

WORKDIR /app

COPY package.json yarn.lock ./

RUN yarn install

COPY . .
RUN yarn build

FROM node:18-alpine AS runner

WORKDIR /app

ARG NUXT_PUBLIC_NODE_ENV=production
ENV NUXT_PUBLIC_NODE_ENV=$NUXT_PUBLIC_NODE_ENV

COPY --from=builder /app/.output ./.output

ENV HOST 0.0.0.0
EXPOSE 3000

# run the build project with node
ENTRYPOINT ["node", ".output/server/index.mjs"]