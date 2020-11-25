# pull official base image
FROM node:14.4.0-alpine3.10

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install app dependencies
COPY package.json ./
COPY package-lock.json ./

RUN npm cache clean --force && npm install react-router-dom && npm install react-icons && npm install axios &&  npm install react-bootstrap

# add app
COPY . ./

# start app
CMD ["npm", "start"]
