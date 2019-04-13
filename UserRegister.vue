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
                <popper trigger="hover" :options = "{placement: 'bottom'}">
                    <div class="popper tw-font-hairline tw-text-grey-dark">
                        What kind of tags do you want to exclude
                    </div>
                    <button slot="reference">   
                        <i class="fas fa-exclamation-circle tw-text-grey-dark tw-cursor-pointer"></i>
                    </button>
                </popper>
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
                <popper trigger="hover" :options = "{placement: 'bottom'}">
                    <div class="popper tw-font-hairline tw-text-grey-dark">
                        Your password should contain a minimum of 6 characters
                    </div>
                    <button slot="reference">   
                        <i class="fas fa-exclamation-circle tw-text-grey-dark tw-cursor-pointer"></i>
                    </button>
                </popper>
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
    import 'vue-popperjs/dist/css/vue-popper.css';
    import Popper from 'vue-popperjs';
    
    export default {
        components: {
            'popper': Popper
        },

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