module.exports = function(grunt) {

  grunt.initConfig({
    responsive_images: {
      dev: {
        options: {
          engine: 'im',
          sizes: [{
            width: 800,
            suffix: 'large-2x',
            quality: 80
          }]
        },

        files: {
          'images-src/computer-pic.jpg':'images-src/computer-pic-small-1170.jpg' 
        }
      }
    },
  });

  grunt.loadNpmTasks('grunt-responsive-images');
  grunt.registerTask('default', ['responsive_images']);

};
