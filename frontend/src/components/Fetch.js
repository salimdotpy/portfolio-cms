const fetchCsrfToken = async () => {
    try {
        const response = await fetch('https://salimtech.pythonanywhere.com/get-csrf-token', {
            method: 'GET',
            credentials: 'include'
        });
        const data = await response.json();
        return data.csrf_token;
    } catch (error) {
        console.error('Error fetching CSRF token:', error);
        return null;
    }
};
const fetchWithCSRF = async (url, options = {}) => {
    const csrfToken = await fetchCsrfToken();

    if (csrfToken) {
        try {
            const response = await fetch(`https://salimtech.pythonanywhere.com/${url}`, {
                ...options,
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken  // Flask-WTF expects the token in the X-CSRFToken header
                },
                credentials: 'include' // Include credentials for CSRF
            });
            return response;
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    }
};

export { fetchWithCSRF, fetchCsrfToken };