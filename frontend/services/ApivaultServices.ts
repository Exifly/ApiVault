import axios, { AxiosInstance } from 'axios';
import { TrendingCategory, APIType, GoogleOAauth2Config } from '../models/types';


class ApivaultService {

    private readonly axiosInstance: AxiosInstance;
    private readonly baseUrl: string = `${import.meta.env.VITE_APIVAULT_SERVICES_ENDPOINT}api`;

    constructor() {
        this.axiosInstance = axios.create({
            baseURL: this.baseUrl,
            headers: {
                'Content-type': 'application/json',
            }
        });
    }

    allApis(): Promise<APIType[]> {
        return this.axiosInstance.get(`${this.baseUrl}/all/`).then(res => res.data);
    }

    apiCategoryData(category: string | string[], authToken: string): Promise<APIType[]> {
        if (authToken === "" || !authToken) return this.axiosInstance.get(`${this.baseUrl}/category/${category}/`).then(res => res.data);

        let headers = {
            'Authorization': `Bearer ${authToken}` 
        }
        return this.axiosInstance.get(`${this.baseUrl}/category/${category}/`, { headers: headers }).then(res => res.data);
    }

    randomApis(): Promise<APIType[]> {
        return this.axiosInstance.get(`${this.baseUrl}/random/`).then(res => res.data)
    }

    countApis(): Promise<number> {
        return this.axiosInstance.get(`${this.baseUrl}/count/`).then(res => res.data.api_count)
    }

    getTrendingCategories(): Promise<TrendingCategory[]> {
        return this.axiosInstance.get(`${this.baseUrl}/categories/trending/`).then(res => res.data);
    }

    sendOAuthConfigToDjango(authToken: String): Promise<GoogleOAauth2Config> {
        return this.axiosInstance.post(`${this.baseUrl}/auth/google/`, {auth_token: authToken}).then(res => res.data);
    }

    async incrementLike(apiId: number, authToken: string): Promise<Number> {
        const headers = {
            'Authorization': `Bearer ${authToken}`
        };

        return await this.axiosInstance.post(`${this.baseUrl}/interaction/like/${apiId}/`, {}, { headers: headers }).then(res => {
          return res.status
        }).catch(err => err.response.status);
    }

}

export default new ApivaultService();
