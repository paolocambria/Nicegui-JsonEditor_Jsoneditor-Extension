export default {
  template: `
    <div></div>
    `,
  data() {
    return {
      editor: null,
      schema: null,
    };
  },
  mounted() {
    this.initializeEditor();
  },
  methods: {
    initializeEditor() {
      const container = this.$el;
      const settings = JSON.parse(JSON.stringify(this.settings));

      this.editor = new JSONEditor(container, settings);
      
      this.editor.on("change", () => {
        this.$emit("change", { content: this.editor.getValue(), errors: this.editor.validate() });
      });
      
      this.editor.on('add', (property) => {
        this.$emit('add', property);
      });

      this.editor.on("switch", (property) => {
        this.$emit("switch", property);
      });

      this.editor.on("addRow", (editor) => {
        this.$emit("addRow", editor);
      });

      this.editor.on("deleteRow", (deletedValue) => {
        this.$emit("deleteRow", deletedValue);
      });

      this.editor.on("deleteAllRows", (deletedValues) => {
        this.$emit("deleteAllRows", deletedValues);
      });



    },
    
    run_update_settings(settings) {
      this.settings = settings;
      if (this.editor) {
        this.editor.setOptions({ settings });
      }
    },    
    run_update_schema(schema) {
      this.schema = schema;
      if (this.editor) {
        this.editor.setSchema(schema);
      }
    },    
    reset() {
    },

  },
  props: {
    settings: Object,
    schema: Object,
  },
};
