import axios, { AxiosInstance } from 'axios'
import {
    TrendingCategory,
    APIType,
    GoogleOAauth2Config,
    Category,
    User,
} from '../models/types'

class ApivaultService {
    private readonly axiosInstance: AxiosInstance
    private readonly baseUrl: string = `${
        import.meta.env.VITE_APIVAULT_SERVICES_ENDPOINT
    }api`

    constructor() {
        this.axiosInstance = axios.create({
            baseURL: this.baseUrl,
            headers: {
                'Content-type': 'application/json',
            },
        })
    }

    allApis(): Promise<APIType[]> {
        return this.axiosInstance
            .get(`${this.baseUrl}/all`)
            .then((res) => res.data)
    }

    apiCategoryData(
        category: string | string[],
        authToken: string,
        orderBy: string
    ): Promise<APIType[]> {
        if (authToken === '' || !authToken)
            return this.axiosInstance
                .get(`${this.baseUrl}/category/${category}?order=${orderBy}`)
                .then((res) => res.data)
        let headers = {
            Authorization: `Bearer ${authToken}`,
        }
        return this.axiosInstance
            .get(`${this.baseUrl}/category/${category}?order=${orderBy}`, {
                headers: headers,
            })
            .then((res) => res.data)
    }

    randomApis(authToken: string): Promise<APIType[]> {
        if (authToken === '' || !authToken)
            return this.axiosInstance
                .get(`${this.baseUrl}/random`)
                .then((res) => res.data)
        let headers = {
            Authorization: `Bearer ${authToken}`,
        }
        return this.axiosInstance
            .get(`${this.baseUrl}/random`, { headers: headers })
            .then((res) => res.data)
    }

    async search(query: String, authToken: String): Promise<APIType[]> {
        if (authToken === '' || !authToken)
            return await this.axiosInstance
                .get(`${this.baseUrl}/search?query=${query}`)
                .then((res) => res.data)
                .catch((err) => err.response.status)
        let headers = { Authorization: `Bearer ${authToken}` }
        return await this.axiosInstance
            .get(`${this.baseUrl}/search?query=${query}`, { headers: headers })
            .then((res) => res.data)
            .catch((err) => err.response.status)
    }

    countApis(): Promise<number> {
        return this.axiosInstance
            .get(`${this.baseUrl}/count`)
            .then((res) => res.data.api_count)
    }

    getTrendingCategories(): Promise<TrendingCategory[]> {
        return this.axiosInstance
            .get(`${this.baseUrl}/categories/trending`)
            .then((res) => res.data)
    }

    /* Not auth layer */
    async categories(): Promise<Category[]> {
        return this.axiosInstance
            .get(`${this.baseUrl}/categories`)
            .then((res) => res.data)
    }

    /* Authentication Layer */
    sendOAuthConfigToDjango(authToken: String): Promise<GoogleOAauth2Config> {
        return this.axiosInstance
            .post(`${this.baseUrl}/auth/google/`, { auth_token: authToken })
            .then((res) => res.data)
    }

    async like(apiId: number, authToken: string): Promise<Number> {
        const headers = {
            Authorization: `Bearer ${authToken}`,
        }

        return await this.axiosInstance
            .post(
                `${this.baseUrl}/interaction/like/${apiId}`,
                {},
                { headers: headers }
            )
            .then((res) => {
                return res.status
            })
            .catch((err) => err.response.status)
    }

    async dislike(apiId: number, authToken: string): Promise<Number> {
        const headers = {
            Authorization: `Bearer ${authToken}`,
        }

        return await this.axiosInstance
            .delete(`${this.baseUrl}/interaction/like/${apiId}`, {
                headers: headers,
            })
            .then((res) => {
                return res.status
            })
            .catch((err) => err.response.status)
    }

    async pendingApis(authToken: string): Promise<APIType[]> {
        const headers = {
            Authorization: `Bearer ${authToken}`,
        }

        return await this.axiosInstance
            .get(`${this.baseUrl}/pending/my_api`, { headers: headers })
            .then((res) => {
                return res.data
            })
            .catch((er) => console.error(er))
    }

    async myApis(authToken: string): Promise<APIType[]> {
        const headers = {
            Authorization: `Bearer ${authToken}`,
        }
        return await this.axiosInstance
            .get(`${this.baseUrl}/my_api`, { headers: headers })
            .then((res) => res.data)
    }

    async submitApi(
        authToken: string,
        name: string,
        auth: string,
        category: number,
        cors: boolean,
        description: string,
        https: boolean,
        url: string
    ): Promise<Number> {
        const headers = {
            Authorization: `Bearer ${authToken}`,
        }

        const data = {
            name: name,
            auth: auth,
            category: category,
            cors: cors,
            description: description,
            https: https,
            url: url,
        }

        return await this.axiosInstance
            .post(`${this.baseUrl}/create`, data, { headers: headers })
            .then((res) => {
                return res.status
            })
            .catch((err) => err.response.status)
    }

    async userInfo(authToken: string): Promise<User> {
        const headers = {
            Authorization: `Bearer ${authToken}`,
        }
        return await this.axiosInstance
            .get(`${this.baseUrl}/auth/user/`, { headers: headers })
            .then((res) => res.data)
    }

    async submitFeedback(
        authToken: string,
        name: string,
        email: string,
        message: string
    ): Promise<Number> {
        const headers = {
            Authorization: `Bearer ${authToken}`,
        }

        const body = {
            name: name,
            email: email,
            message: message,
        }

        return await this.axiosInstance
            .post(`${this.baseUrl}/interaction/feedback`, body, {
                headers: headers,
            })
            .then((res) => res.data.status)
            .catch((er) => er.data.status)
    }
}

export default new ApivaultService()
