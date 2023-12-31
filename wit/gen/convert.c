// Generated by `wit-bindgen` 0.12.0. DO NOT EDIT!
#include "convert.h"


__attribute__((__import_module__("$root"), __import_name__("print")))
extern void __wasm_import_convert_print(int32_t, int32_t);
__attribute__((__weak__, __export_name__("cabi_post_exec")))
void __wasm_export_convert_exec_post_return(int32_t arg0) {
  int32_t ptr = *((int32_t*) (arg0 + 0));
  int32_t len = *((int32_t*) (arg0 + 4));
  for (int32_t i = 0; i < len; i++) {
    int32_t base = ptr + i * 1;
    (void) base;
  }
  if (len > 0) {
    free((void*) (ptr));
  }
}

__attribute__((__weak__, __export_name__("cabi_realloc")))
void *cabi_realloc(void *ptr, size_t old_size, size_t align, size_t new_size) {
  (void) old_size;
  if (new_size == 0) return (void*) align;
  void *ret = realloc(ptr, new_size);
  if (!ret) abort();
  return ret;
}

// Helper Functions

void convert_list_u8_free(convert_list_u8_t *ptr) {
  if (ptr->len > 0) {
    free(ptr->ptr);
  }
}

void convert_string_set(convert_string_t *ret, char*s) {
  ret->ptr = (uint8_t*) s;
  ret->len = strlen(s);
}

void convert_string_dup(convert_string_t *ret, const char*s) {
  ret->len = strlen(s);
  ret->ptr = cabi_realloc(NULL, 0, 1, ret->len * 1);
  memcpy(ret->ptr, s, ret->len * 1);
}

void convert_string_free(convert_string_t *ret) {
  if (ret->len > 0) {
    free(ret->ptr);
  }
  ret->ptr = NULL;
  ret->len = 0;
}

// Component Adapters

__attribute__((__aligned__(4)))
static uint8_t RET_AREA[8];

void convert_print(convert_string_t *msg) {
  __wasm_import_convert_print((int32_t) (*msg).ptr, (int32_t) (*msg).len);
}

__attribute__((__export_name__("exec")))
int32_t __wasm_export_convert_exec(int32_t arg, int32_t arg0) {
  convert_list_u8_t arg1 = (convert_list_u8_t) { (uint8_t*)(arg), (size_t)(arg0) };
  convert_list_u8_t ret;
  convert_exec(&arg1, &ret);
  int32_t ptr = (int32_t) &RET_AREA;
  *((int32_t*)(ptr + 4)) = (int32_t) (ret).len;
  *((int32_t*)(ptr + 0)) = (int32_t) (ret).ptr;
  return ptr;
}

extern void __component_type_object_force_link_convert(void);
void __component_type_object_force_link_convert_public_use_in_this_compilation_unit(void) {
  __component_type_object_force_link_convert();
}
