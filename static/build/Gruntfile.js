'use strict';

module.exports = function(grunt) {

    // Project configuration.
    grunt.initConfig({

        // Metadata.
        pkg: grunt.file.readJSON('package-lock.json'),
        banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n',

        clean: {
            options: {
                force: true
            },
            files: ['../css/*']
        },
        compass: {
            dist: {
                options: {
                    sassDir: 'sass/',
                    cssDir: '../css/',
                    outputStyle: 'compact',
                    noLineComments: true ,
                    bundleExec:true
                }
            },
            localDev: {
                options: {
                    sassDir: 'sass/',
                    cssDir: '../css/',
                    outputStyle: 'expanded',
                    noLineComments: false
                }
            }
        },
        concat:{
            projectMain:{
                src:[
                    'js/test.js',
                    'js/test2.js'
                ],
                dest:'../js/pm001.js',
                nonull: true
            }
        },
        watch: {
            sassy: {
                files: ['sass/*.scss','sass/_partials/*.scss'],
                tasks: ['compass:localDev'],
                options: {
                    spawn: false
                }
            },
            scripts:{
                files:['/js/*'],
                tasks:['concat'],
                options:{
                    spawn:false
                }
            }
        }
    });

    // These plugins provide necessary tasks.
    grunt.loadNpmTasks('grunt-contrib-clean');
    grunt.loadNpmTasks('grunt-contrib-compass');
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-watch');

    // Default task.
    grunt.registerTask('devWatch', ['compass:localDev','watch']);
    grunt.registerTask('firstRun', ['compass:localDev','concat']);
    grunt.registerTask('default', ['clean','compass:dist','concat']);


};