import type { ResponseData } from "./base";

export type BlogData = {
    id: number;
    title: string;
    image_url: string;
    description: string;
    url: string;

    created_at: Date | null;
    updated_at: Date | null;
    children?: BlogData[];
}

export type BlogRsp = ResponseData<BlogData[]>
