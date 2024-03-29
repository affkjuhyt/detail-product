<template>
    <footer class="border-t-4 border-primary-500 footerBg">
        <div class="sr-only">Footer</div>

        <div class="py-8 lg:py-16 px-4 container-v2">
            <div class="xl:grid xl:grid-cols-12 xl:gap-8">
                <div class="xl:col-span-5 xl:mr-10">
                    <div class="flex flex-wrap items-center space-x-2 pb-3">
                        <img alt="Mua Thông Minh" class="h-10" src="~/assets/images/logoAppBeeCost2-01.png" />
                    </div>

                    <p class="text-gray-500 text-base">
                        <span class="">Mua Thông Minh</span>
                        là website, ứng dụng tìm kiếm và đánh giá hàng hóa sản phẩm online. Giúp bạn né Sale ảo, mua giá tốt, tin cậy và trở thành
                        người tiêu dùng thông thái.

                        <span class="font-medium text-gray-600">MuaThongMinh.vn không bán hàng!</span>
                    </p>

                    <p class="mt-3 mb-2 text-gray-500">KẾT NỐI VỚI CHÚNG TÔI</p>

                    <div class="flex space-x-6 pb-2">
                        <a v-for="(social, index) in socialLinks" :href="social.url" :key="index" class="text-gray-400 hover:text-gray-500">
                            <span class="sr-only">{{ social.name }}</span>
                            <component :is="social.icon" class="h-6 w-6" />
                        </a>
                    </div>
                </div>

                <div class="grid grid-cols-1 gap-8 xl:mt-0 xl:col-span-7 mt-12">
                    <div class="md:grid md:grid-cols-2 md:gap-8">
                        <div>
                            <div class="text-sm font-semibold text-gray-400 tracking-wider uppercase">Về Mua Thông Minh</div>

                            <ul class="mt-4 space-y-4">
                                <li>
                                    <a href="https://muathongminh.vn/blog" class="text-base text-gray-500 hover:text-gray-900"> Blog </a>
                                </li>

                                <li>
                                    <a href="https://muathongminh.vn/about" class="text-base text-gray-500 hover:text-gray-900" rel="nofollow"> Giới thiệu </a>
                                </li>

                                <li>
                                    <a href="https://muathongminh.vn/privacy" class="text-base text-gray-500 hover:text-gray-900" rel="nofollow"> Chính sách bảo mật </a>
                                </li>

                                <li>
                                    <a href="https://muathongminh.vn/term" class="text-base text-gray-500 hover:text-gray-900" rel="nofollow"> Điều khoản sử dụng </a>
                                </li>

                                <li>
                                    <a href="https://metric.vn" class="text-base text-gray-500 hover:text-gray-900 cursor-pointer">Metric</a>
                                </li>

                                <li>
                                    <a href="https://diemthi.beecost.vn" target="_blank" rel="nofollow">
                                        <span class="text-base text-gray-500 hover:text-gray-900 cursor-pointer">Điểm thi</span>
                                    </a>
                                </li>
                            </ul>
                        </div>

                        <div class="mt-12 md:mt-0">
                            <div class="text-sm font-semibold text-gray-400 tracking-wider uppercase">Liên hệ</div>
                            <ul class="mt-4 space-y-1">
                                <li>
                                    <p class="text-base text-gray-500 font-semibold">Công ty Cổ phần Khoa học Dữ liệu</p>
                                </li>

                                <li><p class="text-base text-gray-500">Số ĐKKD: 0108677693</p></li>

                                <li>
                                    <p class="text-base text-gray-500">
                                        Địa chỉ: Tầng 6 toà nhà AZ Lâm Viên, 107A Nguyễn Phong Sắc, Phường Dịch Vọng Hậu, Quận Cầu Giấy, Thành phố Hà
                                        Nội, Việt Nam.
                                    </p>
                                </li>

                                <li><p class="text-base text-gray-500">Email: info@beecost.com</p></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>

            <div class="flex flex-col justify-center items-center mt-4 border-t border-gray-200 pt-4">
                <div class="flex flex-wrap text-gray-500 items-center justify-center my-2 text-sm">
                    <span>Quốc gia &amp; Khu vực: </span>

                    <a v-for="(country, index) in countries" :href="country.url" :key="index" target="_self" rel="noopener"
                        :title="country.name" class="hover:text-gray-600 px-2">
                        {{ country.name }}
                    </a>
                </div>
            </div>
        </div>
    </footer>
</template>

<script setup lang="ts">
import FacebookIcon from '~/assets/icons/facebook.svg';
import InstagramIcon from '~/assets/icons/instagram.svg';
import GithubIcon from '~/assets/icons/github.svg';

const socialLinks = [
    { name: 'Facebook', url: 'https://facebook.com/beecostvn', icon: FacebookIcon },
    { name: 'Instagram', url: 'https://instagram.com/beecostprice', icon: InstagramIcon },
    { name: 'GitHub', url: 'https://github.com/beecost', icon: GithubIcon }
]

const countries = [
  { name: 'Việt Nam', url: 'https://beecost.vn' },
  { name: 'Singapore', url: 'https://beecost.sg' },
  { name: 'Philippines', url: 'https://beecost.ph' },
  { name: 'Malaysia', url: 'https://beecost.com.my' },
  { name: 'Indonesia', url: 'https://beecost.co.id' },
  { name: 'Đài Loan', url: 'https://beecost.tw' },
  { name: 'Mexico', url: 'https://beecost.com.mx' },
  { name: 'Brazil', url: 'https://beecost.com.br' },
  { name: 'Thái Lan', url: 'https://thai.beecost.com' }
];

defineComponent({
    name: 'FooterComponent',
});
</script>

<style scoped>
.footerBg {
    background-color: rgb(245, 245, 245);
}
</style>
