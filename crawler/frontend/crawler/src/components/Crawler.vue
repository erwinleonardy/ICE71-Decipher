<template>
    <div>
        <div class="form-group row">
            <label for="url" class="col-md-4 col-form-label text-md-right">
                url 
            </label>

            <div class="col-md-6">
                <input type = "text"
                    id="url" 
                    v-model = "url"
                    class="tw-border tw-rounded tw-p-2 tw-w-full tw-border-grey" 
                    :class = "{ 'tw-border-red-light' : error['url'] != undefined}"
                    placeholder = "S4123451E"
                    required autofocus
                >
            </div>
        </div>
        
        <!-- exclude -->
        <div class="form-group row">
            <label for="exclude" class="col-md-4 col-form-label text-md-right">
                exclude
            </label>

            <div class="col-md-6">
                <input type = "exclude"
                    id="exclude" 
                    v-model = "exclude"
                    class="tw-border tw-rounded tw-p-2 tw-w-full tw-border-grey" 
                    :class = "{ 'tw-border-red-light' : error['exclude'] != undefined}"
                    oncopy="return false" oncut="return false" onpaste="return false"
                    required autofocus
                >
            </div>
        </div>

        <!-- Password -->
        <div class="form-group row">
            <label for="password" class="col-md-4 col-form-label text-md-right">
                Password
            </label>

            <div class="col-md-6">
                <input type = "password"
                    id="password" 
                    v-model = "password"
                    class="tw-border tw-rounded tw-p-2 tw-w-full tw-border-grey" 
                    :class = "{ 'tw-border-red-light' : error['password'] != undefined}"
                    oncopy="return false" oncut="return false" onpaste="return false"
                    required autofocus
                >
            </div>
        </div>

        <div class="form-group row tw-my-6">
            <div class="col-md-6 offset-md-4">
                <div v-if = "!isLoading">
                    <button type="submit" class="btn btn-primary" @click ="register()" >
                        Register
                    </button>
                </div>
                <div v-else>
                    <img src = "/assets/img/loader.gif" alt = "Loading...">
                </div>
            </div>
        </div>
    </div>
</template>

<script>

    export default {
        name: 'Crawler',

        data() {
            return {
                url: '',
                error: [],
                isLoading: false,
            }
        },

        methods: {
            crawl() {
                this.isLoading = true;

                axios.post("/crawl", {
                    url: this.url,
                    exclude: this.exclude
                })
                .then(response => {
                    //    this.$router.replace( "/login");
                    this.isLoading = false;
                })
                .catch((error) => {
                    // this.error = error.response.data.errors;
                    this.isLoading = false;
                });
            },
        }
    }
</script>