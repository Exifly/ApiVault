import { GithubContributor } from '../models/types'
import axios, { AxiosInstance } from 'axios'

class GithubService {
    private readonly axiosInstance: AxiosInstance
    private readonly baseUrl: string = import.meta.env.VITE_GITHUB_ENDPOINT

    constructor() {
        this.axiosInstance = axios.create({
            baseURL: this.baseUrl,
            headers: {
                'Content-type': 'application/json',
            },
        })
    }

    contributors(): Promise<GithubContributor[]> {
        return this.axiosInstance
            .get(`${this.baseUrl}/repos/exifly/apivault/contributors`)
            .then((res) => res.data)
            .catch((er) => {
                console.error(er)
                return []
            })
    }

    async repoStars(): Promise<number> {
        const repo: globalThis.Ref<any> = ref(null)
        const { data: fetchedData, error } = await useLazyFetch<any>(
            'https://api.github.com/repos/exifly/apivault'
        )
        if (!error) {
            let num: globalThis.Ref<any> = ref(0)
            return num.value
        }
        repo.value = fetchedData.value.stargazers_count
        return repo.value
    }
}

export default new GithubService()
