<template>
    <div id ="testing">
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
                    <div class = "w-full mb-4" v-if = "tokenizeWord.length > 0">
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
                    <div v-if = "tokenizeWord.length > 0">
                        <div class="flex items-center my-4">                
                            <div class = "w-48 ml-32 text-lg font-semibold font-montserrat text-grey-dark">
                                Filtered password
                            </div>

                            <div class="">
                                <input type ="text"
                                    id="filtered" 
                                    v-model = "filtered"
                                    class="border rounded p-2 w-full border-grey" 
                                    required autofocus
                                    disabled
                                >
                            </div>
                        </div>

                        <div class="flex items-center my-4">                
                            <div class = "w-48 ml-32 text-lg font-semibold font-montserrat text-grey-dark">
                                Enthropy
                            </div>

                            <div class="">
                                <input type ="text"
                                    id="enthropy" 
                                    v-model = "enthropy"
                                    class="border rounded p-2 w-full border-grey" 
                                    required autofocus
                                    disabled
                                >
                            </div>
                        </div>

                        <div class="flex items-center my-4">                
                            <div class = "w-48 ml-32 text-lg font-semibold font-montserrat text-grey-dark">
                                True Enthropy
                            </div>

                            <div class="">
                                <input type ="text"
                                    id="trueEnthropy" 
                                    v-model = "trueEnthropy"
                                    class="border rounded p-2 w-full border-grey" 
                                    required autofocus
                                    disabled
                                >
                            </div>
                        </div>

                        <div class="flex items-center my-4">                
                            <div class = "w-48 ml-32 text-lg font-semibold font-montserrat text-grey-dark">
                                Password Strength
                            </div>

                            <div class="">
                                <meter :value="strPercentile"></meter><br>
                                {{this.strength}}
                            </div>
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
                dictionary: '',
                tokenizeWord: [],
                filtered: '',
            }
        },

        watch:{
            dictionary() {
                var tmp = this.dictionary.substr(5).slice(0, -1);
                tmp = tmp.toLowerCase();
                this.tokenizeWord = tmp.split(' ');
                this.tokenizeWord = this.tokenizeWord.sort(function(a, b){
                    return b.length - a.length;
                });
            },
        },

        computed:{
            length() {
                return this.filtered.length;
            },

            trueEnthropy() {
                return this.scorePassword(this.filtered.toLowerCase());  
            },

            strPercentile() {
                return this.trueEnthropy/150;
            },

            enthropy() {
                return this.scorePassword(this.password.toLowerCase());  
            },
            
            strength() {
                if(this.enthropy > 80)
                    return "strong";
                else if(this.entropy > 60 )
                    return "good";
                else
                    return "weak";
                
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

                var scope = this;

                $.ajax({
                    type: 'post',
                    url: 'http://127.0.0.1:5000/crawl',
                    // data: fd,
                    data: $('#myForm').serialize() + "&url=" + this.url + "&exclude=" + this.exclude,
                    mimeType: "multipart/form-data",
                //     // contentType: false,
                    success: function(data, status, jqXHR) {
                        console.log(data)
                        scope.isLoading = false;
                        scope.dictionary = data;
                    },
                    error: function(jqXHR, status, err) {
                        console.log(err);
                        scope.isLoading = false;
                    },
                    complete: function(jqXHR, status) {
                        scope.isLoading = false;
                    }
                })

            },

            verifyPassword() {
                var str = this.password.toLowerCase();    
                console.log(str);
                this.tokenizeWord.forEach(word =>{
                    var tmpWord = word.toLowerCase();

                    var regex = new RegExp( tmpWord, 'g' );
                    var result = str.match(regex);
                    console.log(result);

                    if (result){
                        console.log(result);
                        str = str.replace(word.toLowerCase(),'');
                    }
                });
                this.filtered = str;
            },

            scorePassword(pass) {
                var score = 0;
                if (!pass)
                    return score;

                // award every unique letter until 5 repetitions
                var letters = new Object();
                for (var i=0; i<pass.length; i++) {
                    letters[pass[i]] = (letters[pass[i]] || 0) + 1;
                    score += 5.0 / letters[pass[i]];
                }

                // bonus points for mixing it up
                var variations = {
                    digits: /\d/.test(pass),
                    lower: /[a-z]/.test(pass),
                    upper: /[A-Z]/.test(pass),
                    nonWords: /\W/.test(pass),
                }

                var variationCount = 0;
                for (var check in variations) {
                    variationCount += (variations[check] == true) ? 1 : 0;
                }
                score += (variationCount - 1) * 10;

                return parseInt(score);
            }
        }
    }
</script>