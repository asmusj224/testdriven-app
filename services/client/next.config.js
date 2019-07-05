const { REACT_APP_USERS_SERVICE_URL } = process.env;

module.exports = {
    publicRuntimeConfig: {
        REACT_APP_USERS_SERVICE_URL,
    },
    exportPathMap: () => ({
        '/': { page: '/index' },
    })
};
