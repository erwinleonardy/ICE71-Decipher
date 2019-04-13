<template>
    <div>
        <div class="h-24 mb-4">
            <img class ="h-24" src = "../assets/img/crawler.png" alt = "Crawl">
        </div>

        <div class="row justify-center mb-8">
            <div class="w-2/5">
                <div class="card">
                    <div class="card-header tw-text-grey-darker">Crawl baby</div>

                    <div class = "w-full my-4">
                        <div class = "flex items-center">                         
                            <div class = "w-48 ml-32 text-lg font-semibold font-montserrat text-grey-dark">
                                Numbers of url<span class = "text-red">*</span>
                            </div>

                            <div class = "col-md-1">
                                <select v-model = "numberOfURL" class = "bg-blue-lightest w-14 h-12 border border-solid p-1"> 
                                    <option v-for = "index in 5" :key = "index" class = "bg-blue-lightest"> 
                                        {{index}} 
                                    </option>
                                </select>
                            </div>
                        </div>
                    </div>     

                    <div v-if = "numberOfURL != 0" class = "w-full mb-4">
                        <div class = "flex items-center">                         
                            <div class = "w-48 ml-32 text-lg font-semibold font-montserrat text-grey-dark">
                                URL<span class = "text-red">*</span>
                            </div>
                            <div class="w-3/5 col-md-6">
                                <div v-for = "index in parseInt(numberOfURL)" :key = "index" class="form-group row">
                                    <url
                                        :index = "index"
                                        @updateURLS = "updateURLS"
                                    >
                                    </url>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- exclude -->
                    <div class = "w-full mb-4">
                        <div class = "flex items-center">                         
                            <div class = "w-48 ml-32 text-lg font-semibold font-montserrat text-grey-dark">
                                Exclude
                            </div>

                            <div class="col-md-6">
                                <input type = "text"
                                    id="exclude" 
                                    v-model = "exclude"
                                    class="border rounded p-2 w-full border-grey" 
                                    required autofocus
                                >
                            </div>
                        </div>
                    </div>        

                    <div class="form-group row my-6 justify-center flex">
                        <div v-if = "!isLoading">
                            <button type="button" class="bg-blue hover:bg-blue-dark text-white font-bold py-2 px-4 rounded" @click ="crawl()" >
                                Crawl 
                            </button>
                        </div>
                        <div v-else>
                            <img src = "../assets/img/loader.gif" alt = "Loading...">
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="row justify-content-center mb-4">
            <div class="w-2/5">
                <div class="card">
                    <div class="card-header tw-text-grey-darker">Test password</div>
                    <div class = "w-full mb-4" v-if = "dictionary.length == 0">
                        <div class="flex items-center my-4">                
                            <div class = "w-48 ml-32 text-lg font-semibold font-montserrat text-grey-dark">
                                Password
                            </div>

                            <div class="">
                                <input type ="text"
                                    id="password" 
                                    v-model = "password"
                                    class="border rounded p-2 w-full border-grey" 
                                    required autofocus
                                >
                            </div>
                        </div>

                        <div class="flex justify-center">
                            <div v-if = "!isLoading">
                                <button type="button" class="bg-blue hover:bg-blue-dark text-white font-bold py-2 px-4 rounded" @click ="verifyPassword()" >
                                    Is my password lame?  
                                </button>
                            </div>
                            <div v-else>
                                <img src = "../assets/img/loader.gif" alt = "Loading...">
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>


        <div class="row justify-content-center">
            <div class="w-2/5">
                <div class="card">
                    <div class="card-header tw-text-grey-darker">Results</div>
                    <div class="flex items-center my-4">                
                        <div class = "w-48 ml-32 text-lg font-semibold font-montserrat text-grey-dark">
                            Result
                        </div>

                        <div class="">
                            <input type ="text"
                                id="password" 
                                v-model = "password"
                                class="border rounded p-2 w-full border-grey" 
                                required autofocus
                            >
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </div>
</template>

<script>
    
    import url from './url';
    export default {
        components:{
            'url': url
        },

        name: 'Crawler',

        data() {
            return {
                password:'',
                numberOfURL:'',
                isLoading: false,

                url: [],
                exclude: '',
                
                dictionary: [],
            }
        },

        methods: {
            
            updateURLS(payload) {
                console.log(payload);
                let tmp = this.url;
                this.url[payload.index - 1] = payload.url;
            },

            crawl() {
                this.isLoading = true;

            //     $.ajax({
            //         url: "http://127.0.0.1:5000/api/arne/is/gay/and/bachelor",
            //         type: "POST",
            //         crossDomain: true,
            //         dataType: 'jsonp',
            //     success: function(data, status, jqXHR) {
            //         console.log(data)
            //         // scope.$emit("get-toggle-data", data);
            //     },
            //     error: function(jqXHR, status, err) {
            //         console.log(err);
            //     },
            //     complete: function(jqXHR, status) {}
            // });

            //     axios.get("https://data.gov.sg/api/action/datastore_search?resource_id=8b94f596-91fd-4545-bf9e-7a426493b674&limit=5")
            //     .then(res => {
            //         console.log(res);
            //     })


                const config = {
                    headers: { 'Access-Control-Allow-Origin': '*' , 'content-type': 'application/json; charset=utf-8' }
                };

                axios.post("http://127.0.0.1:5000/crawl", {
                    url: this.url,
                    exclude: this.exclude
                },config)
                .then(response => {
                    console.log(response);
                    this.dictionary = response.data.dictionary;
                    this.isLoading = false;
                    //    this.$router.replace( "/action?");
                })
                .catch((error) => {
                    // this.error = error.response.data.errors;
                    this.isLoading = false;
                });
            },
        }
    }
</script>