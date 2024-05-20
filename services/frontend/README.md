# backup_bumblebee

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

### Dependencies

This project utilizes various dependencies for its operation. To ensure the security of production dependencies and mitigate potential vulnerabilities, it is recommended to regularly run the following command at the root of the project:

```bash
npm audit fix --only=prod
```

### Tests
To run the tests with vite you must use the following command
```bash
npm run test 
```
The test files must go in src/__tests__
and end in ```spec.ts ```