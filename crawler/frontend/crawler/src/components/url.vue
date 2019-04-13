<template>
    <div class="col-md-12">
        <input  
            id="url" 
            v-model = "url"
            class="border rounded p-2 w-full border-red-light" 
            :class = "{ 'border-red-light' : error == true}"
            placeholder = "www.facebook.com/Arne/is/gay"
            required autofocus
        >
    </div>
</template>

<script>

    export default {
        name: 'Crawler',

        props: ['index'],

        data() {
            return {
                url: '',
                error: true,
            }
        },
        
        watch:{
            url() {
                this.$emit('updateURLS', {
                    url: this.url,
                    index: this.index
                });
            }
        },

        computed:{
            // error() {
            //     return true;
            // }
        }
    }
</script>